# **Document Management System Design**

A production-ready document management system similar to Google Drive, Dropbox, or OneDrive with hierarchical storage, version control, and permission management.

## **Requirements**

### **Functional Requirements**

What the system must do \- features and actions:

* **File & Folder Management:** Create, read, update, delete files and folders in hierarchical structure  
* **Version History:** Track all versions of files with ability to restore previous versions  
* **Permissions:** Support read, write, and admin permissions with inheritance through folder hierarchy  
* **Sharing:** Share files/folders with other users or via public links  
* **Search:** Full-text search across file names and metadata  
* **Tags:** Organize files with custom tags  
* **Trash/Recovery:** Soft delete with 30-day recovery period

### **Non-Functional Requirements**

* **Performance:** Sub-100ms response times for common operations (list folders, permission checks)  
* **Scalability:** Support 10M+ users, 1B+ files, 100K concurrent users  
* **Reliability:** 99.9% uptime with automated backups  
* **Storage Efficiency:** Deduplication to reduce storage costs by 40-70%  
* **Compliance:** Audit logging for regulatory requirements (GDPR, HIPAA)

### **Assumptions**

* **Database:** PostgreSQL for metadata with proper indexing and query optimization  
* **Blob Storage:** S3-compatible object storage for actual file content  
* **Read-Heavy Workload:** 90% reads, 10% writes \- optimize for read performance  
* **Folder Depth:** Maximum 20 levels deep to prevent performance degradation  
* **Network:** Reliable network with CDN for global file delivery

## **Core Components**

### **Data Model: Unified Items Table (Polymorphic Pattern)**

**Problem:** Separate files and folders tables create complex JOINs and duplicate permission logic.  
**Solution: Unified Items Table**

* Store both files and folders in single items table with item\_type column ('file' or 'folder')  
* Self-referencing via parent\_id creates hierarchy (adjacency list pattern)  
* Consistent permission model applies to both types  
* Easy to extend with new types (shortcuts, bookmarks, etc.)

**Trade-off:** Some columns only apply to files (current\_version\_id) resulting in NULL values for folders, but this overhead is minimal compared to JOIN complexity.

### 

### **Hierarchy: Adjacency List \+ Materialized Path**

**Problem:** Pure adjacency list requires slow recursive queries for path lookups. Pure materialized path complicates moves.  
**Solution: Hybrid Approach**

* **Adjacency list (parent\_id):** Simple for inserts, updates, moves  
* **Materialized path (full\_path):** Instant path lookups without recursion  
* Both representations maintained in sync

**Performance:**

* Path lookup: O(1) index scan on full\_path  
* Move operation: Update parent\_id \+ full\_path for item and all descendants  
* List children: Simple WHERE parent\_id \= X query

**Trade-off:** Must update full\_path when folders move/rename, but this is infrequent compared to reads.

### 

### **Storage: Content-Addressable with Deduplication**

**Problem:** Storing duplicate file content wastes storage. Same file uploaded by different users should be stored once.  
**Solution: Content-Addressable Blob Storage**

* Calculate SHA-256 checksum for each file version  
* Store blob once per unique checksum in blob\_storage table  
* File versions reference blob via checksum (foreign key)  
* Maintain reference\_count \- only delete blob when count reaches zero  
* Typical storage savings: 40-70%

**Example:**

* Version 1: "Hello" → blob\_abc123 (ref\_count: 1\)  
* Version 2: "Hello World" → blob\_def456 (ref\_count: 1\)  
* Version 3: "Hello" → blob\_abc123 (ref\_count: 2, reuses existing blob)

**Trade-off:** Complexity in managing reference counts atomically. Requires periodic reconciliation job to detect drift.

### 

### **Versioning: Lightweight Metadata-Only Versions**

**Problem:** Storing full copy of each version wastes storage when content rarely changes.  
**Solution: Version References to Blob Storage**

* file\_versions table stores metadata only (version\_number, created\_at, created\_by)  
* Each version points to blob\_storage via checksum  
* Multiple versions can share same blob if content identical  
* Items table has current\_version\_id pointer for fast access to latest version

**Trade-off:** Deleting items requires careful reference counting. Must handle concurrent operations with transactions.

### **Permissions: Materialized View for Effective Permissions**

**Problem:** Permission checks happen on every file access. Recursive queries to check inherited permissions are too slow at scale.  
**Solution: Materialized View**

* permissions table stores explicit grants (item\_id, user\_id, permission\_type)  
* effective\_permissions materialized view precomputes all inherited permissions  
* Permission check becomes simple index lookup instead of recursive query  
* Owner always has implicit admin permission (included in materialized view)

**Performance Impact:**

* Without materialized view: 500ms+ for deep hierarchies  
* With materialized view: \<10ms (simple index scan)

**Refresh Strategy:**

* On permission change: REFRESH MATERIALIZED VIEW CONCURRENTLY  
* Scheduled: Every 5 minutes via background job  
* Requires unique index on (item\_id, user\_id) for concurrent refresh

**Permission Types:**

* **read:** View and download files  
* **write:** Edit files, upload new versions  
* **admin:** Delete, manage permissions

**Trade-off:** Eventual consistency \- recent permission changes may take up to 5 minutes to propagate. For critical use cases, can trigger immediate refresh.

### 

### **Deletion: Soft Delete with Trash Bin**

**Problem:** Accidental deletes are common. Hard deletes make recovery impossible.  
**Solution: Soft Delete Pattern**

* Add deleted\_at timestamp column (NULL for active items)  
* Delete operation sets deleted\_at instead of removing row  
* All queries filter WHERE deleted\_at IS NULL  
* Background job permanently deletes items after 30 days  
* Restore operation simply sets deleted\_at \= NULL

**Trade-off:** Must remember to filter deleted items in all queries. Create active\_items view to simplify.

### 

### **Organization: Normalized Tags Table**

**Problem:** Storing tag names with each item wastes space and creates inconsistencies ("Important" vs "important").  
**Solution: Normalized Tag Schema**

* tag\_names table stores each unique tag once  
* item\_tags junction table for many-to-many relationship  
* Enables tag autocomplete and prevents typos  
* Can track tag popularity/usage counts  
* Storage savings: \~90% vs storing tag names per item

### **Sharing: UUID-Based Share Links**

**Problem:** Need public sharing without requiring user accounts. Sequential IDs are guessable.  
**Solution: Cryptographically Secure Tokens**

* Use gen\_random\_uuid() for unguessable tokens  
* Optional password protection and expiration  
* Track access for analytics  
* Rate limiting prevents abuse

**Security:** Never use sequential IDs. Always rate limit access attempts. Auto-expire unused links after 30 days.

### 

### **Compliance: Append-Only Audit Log**

**Problem:** Regulatory requirements (GDPR, HIPAA) mandate tracking all actions.  
**Solution: Immutable Audit Log**

* Log all actions: create, read, update, delete, share, permission changes  
* Store: user\_id, item\_id, action\_type, timestamp, metadata (JSONB)  
* Append-only table (no UPDATEs allowed)  
* Partition by date (monthly) for performance  
* Archive to data warehouse after 90 days

**Trade-off:** High write volume. Large table growth requires archival strategy.

### 

### **Resource Management: Per-User Storage Quotas**

**Problem:** Need to prevent abuse and enable monetization through storage tiers.  
**Solution: Tracked Storage Usage**

* Users table has storage\_used\_bytes and storage\_quota\_bytes columns  
* Update atomically with file operations (within same transaction)  
* Periodic reconciliation job (weekly) to detect drift  
* Alert when \>5% drift detected

## **Request Flow**

### **Upload File Flow (Write Operation)**

1. **Client initiates upload:** Application receives file and calculates SHA-256 checksum  
2. **Check deduplication:** Query blob\_storage to see if checksum already exists  
3. **Upload to S3 (if new):** If checksum not found, upload file to S3 blob storage  
4. **Database transaction:**  
   * Insert/update blob\_storage (increment reference\_count)  
   * Insert new file\_versions record  
   * Update items.current\_version\_id pointer  
   * Update users.storage\_used\_bytes  
   * Insert audit\_log entry  
5. **Return success:** Send confirmation to client with file metadata

### **Download File Flow (Read Operation)**

6. **Client requests file:** Application receives request with item\_id  
7. **Permission check:** Query effective\_permissions materialized view (\<10ms)  
8. **Get file metadata:** Fetch item and current version from database  
9. **Generate presigned URL:** Create temporary S3 presigned URL (1 hour expiration)  
10. **Return to client:** Client downloads directly from S3 (no proxy through app server)  
11. **Log access:** Insert audit\_log entry asynchronously

### **List Folder Contents Flow**

12. **Client requests folder:** Application receives folder\_id  
13. **Permission check:** Verify read permission via materialized view  
14. **Query children:** SELECT \* FROM items WHERE parent\_id \= folder\_id AND deleted\_at IS NULL ORDER BY item\_name  
15. **Apply pagination:** Use cursor-based pagination (not OFFSET) for large folders  
16. **Return results:** Send metadata (name, size, modified date, type) to client (\<50ms)

### **Move Item Flow**

17. **Client initiates move:** Request to move item to new parent folder  
18. **Permission check:** Verify write permission on both source and destination  
19. **Validate move:** Ensure not moving folder into its own descendant (prevent cycles)  
20. **Database transaction:**  
    * Update items.parent\_id  
    * Recalculate and update full\_path for item and all descendants  
    * Insert audit\_log entry  
21. **Refresh permissions:** Trigger materialized view refresh if permissions may have changed  
22. **Return success:** Confirm move completed

### **Delete File Flow (Soft Delete)**

23. **Client initiates delete:** Request to delete item  
24. **Permission check:** Verify admin permission  
25. **Soft delete:** UPDATE items SET deleted\_at \= NOW() WHERE id \= item\_id  
26. **Cascade to children:** If folder, mark all descendants as deleted  
27. **Insert audit log:** Record deletion event  
28. **Background job (after 30 days):**  
    * Decrement blob\_storage.reference\_count  
    * Delete blob from S3 if reference\_count \= 0  
    * Hard delete item from database (CASCADE to versions, permissions)  
    * Update users.storage\_used\_bytes

## **Scaling Considerations**

### **What Would Break at Scale**

**1\. Deep Folder Nesting (100+ levels)**  
**Problem:** Recursive path updates become exponentially slow.  
**Solutions:**

* Enforce max depth of 20 levels in UI and API  
* Use materialized path exclusively for deep hierarchies  
* Show warning when approaching limit

**2\. Permission Check Latency**  
**Problem:** Every file access requires database query for permission.  
**Solutions:**

* Cache permissions in Redis with 5-minute TTL  
* Include basic permissions in JWT token payload  
* Batch permission checks when listing multiple files  
* Use read replicas for permission queries

**3\. Large Folders (100K+ files)**  
**Problem:** Listing contents returns huge result set, slow query.  
**Solutions:**

* Use cursor-based pagination instead of OFFSET (much faster)  
* Index on (parent\_id, created\_at) for efficient pagination  
* Implement virtual scrolling in UI  
* Lazy load thumbnails and metadata

**4\. Version Accumulation (1000+ versions)**  
**Problem:** file\_versions table grows huge, slowing queries.  
**Solutions:**

* Limit to last 50 versions per file (configurable by tier)  
* Auto-delete versions \>1 year old  
* Archive older versions to cheaper storage (Glacier)  
* Index on (item\_id, version\_number DESC) for fast latest version lookup

**5\. Materialized View Refresh Performance**  
**Problem:** Large refreshes cause latency spikes.  
**Solutions:**

* Use REFRESH MATERIALIZED VIEW CONCURRENTLY (non-blocking)  
* Implement incremental updates via triggers instead of full refresh  
* Schedule refreshes during low-traffic periods  
* Accept 5-minute eventual consistency delay

**6\. Blob Reference Counting Race Conditions**  
**Problem:** Concurrent operations can corrupt reference counts.  
**Solutions:**

* Use database transactions for all blob operations  
* Implement row-level locks (SELECT ... FOR UPDATE)  
* Weekly reconciliation job: compare reference\_count vs actual usage  
* Alert on any discrepancies \>5%

**7\. Orphaned Blobs in S3**  
**Problem:** Database thinks blob exists, but S3 file deleted or corrupted.  
**Solutions:**

* Regular reconciliation: compare blob\_storage table vs S3 bucket inventory  
* Store checksum in S3 object metadata for validation  
* Validate checksum on download, re-upload if mismatch  
* Enable S3 versioning as backup safety net

**8\. Audit Log Growth**  
**Problem:** Billions of rows after years of operation.  
**Solutions:**

* Partition table by month/year  
* Archive to data warehouse (Snowflake/BigQuery) after 90 days  
* Use separate database cluster for audit logs  
* Retention policy: delete after 7 years (compliance requirement)

**9\. Share Link Abuse**  
**Problem:** Public links getting scraped, excessive downloads.  
**Solutions:**

* Rate limiting: max 100 requests per token per hour  
* CAPTCHA after N failed password attempts  
* Auto-expire links after 30 days of no use  
* Suspicious pattern detection (IP address, user agent)

**10\. Storage Quota Drift**  
**Problem:** storage\_used\_bytes out of sync with actual usage.  
**Solutions:**

* Database triggers on version create/delete to update quota atomically  
* Weekly background reconciliation job  
* Alert when \>5% drift detected  
* Transaction rollback on quota exceeded

## **Performance Benchmarks**

**Expected with proper indexing:**

| Operation | Latency | Notes |
| :---- | :---- | :---- |
| List folder (50 items) | \<50ms | Index on parent\_id |
| Check permission | \<10ms | Materialized view |
| Search by name | \<100ms | GIN index |
| Upload file (10MB) | \<2s | S3 latency dominant |
| Get version history | \<20ms | Direct query |

**Scaling targets:**

* 10M users  
* 1B files  
* 100K concurrent users  
* 10K uploads/second  
* 100K permission checks/second
