# API Design

## 📐 Core Principles

| Principle | Description |
|-----------|-------------|
| **Consistency** | Same patterns, naming, and error shapes everywhere |
| **Predictability** | Consumers can guess endpoints they haven't used |
| **Versioning** | Never break existing clients |
| **Idempotency** | Safe to retry without side effects |
| **Least surprise** | Do what the name says, nothing more |

---

## 🗂️ Resource Naming

### URL Structure

```
/api/v1/{resource}/{id}/{sub-resource}
```

**Good:**
```
GET    /api/v1/users/123
GET    /api/v1/users/123/posts
POST   /api/v1/users/123/posts
DELETE /api/v1/posts/456
```

**Bad:**
```
GET  /api/v1/getUser?id=123
POST /api/v1/user/createPost
GET  /api/v1/user/123/getFollowers
```

### Rules
- Use **nouns**, not verbs (the HTTP method is the verb)
- Use **plural** resource names (`/users`, not `/user`)
- Use **kebab-case** for multi-word resources (`/blog-posts`)
- Nest sub-resources max **1–2 levels** deep

---

## 📬 HTTP Methods

| Method | Use | Idempotent | Body |
|--------|-----|-----------|------|
| `GET` | Read resource | ✅ | ❌ |
| `POST` | Create resource | ❌ | ✅ |
| `PUT` | Replace resource (full) | ✅ | ✅ |
| `PATCH` | Partial update | ❌ | ✅ |
| `DELETE` | Remove resource | ✅ | ❌ |

**Use `PUT` for full replacement, `PATCH` for partial updates:**

```http
# Update only the email
PATCH /api/v1/users/123
{ "email": "new@example.com" }

# Replace the whole resource
PUT /api/v1/users/123
{ "id": 123, "email": "new@example.com", "name": "Jane" }
```

---

## ✅ Response Shapes

### Success — Single Resource

```json
{
  "data": {
    "id": 123,
    "username": "johndoe",
    "email": "john@example.com",
    "created_at": "2025-01-15T10:30:00Z"
  }
}
```

### Success — Collection

```json
{
  "data": [...],
  "meta": {
    "total": 1240,
    "page": 1,
    "per_page": 20,
    "pages": 62
  },
  "links": {
    "self":  "/api/v1/posts?page=1",
    "next":  "/api/v1/posts?page=2",
    "prev":  null,
    "first": "/api/v1/posts?page=1",
    "last":  "/api/v1/posts?page=62"
  }
}
```

### Error

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      { "field": "email", "message": "Invalid email format" },
      { "field": "age",   "message": "Must be at least 18" }
    ],
    "request_id": "req_8f3kd92"
  }
}
```

**Always include `request_id`** — makes debugging and support much easier.

---

## 🚦 HTTP Status Codes

| Code | Meaning | When |
|------|---------|------|
| `200` | OK | Successful GET, PUT, PATCH |
| `201` | Created | Successful POST |
| `202` | Accepted | Async operation queued |
| `204` | No Content | Successful DELETE |
| `400` | Bad Request | Validation error |
| `401` | Unauthorized | Missing/invalid auth |
| `403` | Forbidden | Authenticated but not allowed |
| `404` | Not Found | Resource doesn't exist |
| `409` | Conflict | Duplicate / state conflict |
| `422` | Unprocessable Entity | Semantic validation failure |
| `429` | Too Many Requests | Rate limit hit |
| `500` | Internal Server Error | Unexpected server fault |

> Use `404` for missing resources, `403` for permission denied — never swap them.

---

## 🔢 Pagination

### Prefer Cursor-Based for Large / Real-Time Data

```
GET /api/v1/posts?cursor=eyJpZCI6MTAwfQ&limit=20
```

```json
{
  "data": [...],
  "meta": {
    "next_cursor": "eyJpZCI6ODB9",
    "has_more": true
  }
}
```

**Why cursor over offset:** page 50 of a live feed shifts as new items arrive; cursors stay stable.

### Offset Pagination (Fine for Admin / Static Data)

```
GET /api/v1/users?page=3&per_page=25
```

### Rules
- Default page size: **20**, max: **100**
- Never allow unbounded queries (`limit=0` or no limit)

---

## 🔍 Filtering, Sorting, Searching

```
# Filter
GET /api/v1/posts?status=published&author_id=123

# Sort (prefix - for descending)
GET /api/v1/posts?sort=-created_at,title

# Search
GET /api/v1/posts?q=backend+scaling

# Field selection (sparse fieldsets)
GET /api/v1/users?fields=id,username,avatar_url
```

---

## 🔐 Versioning

### URI Versioning (Recommended)

```
/api/v1/users
/api/v2/users
```

**Simple, explicit, easy to route and deprecate.**

### Header Versioning (Alternative)

```http
GET /api/users
Accept: application/vnd.myapp.v2+json
```

### Rules
- Never remove fields — mark them `deprecated` first
- Maintain old versions for at least **6 months** after deprecation notice
- Use `Sunset` response header to communicate removal date:

```http
Sunset: Sat, 31 Dec 2025 23:59:59 GMT
Deprecation: true
Link: <https://docs.example.com/migration/v2>; rel="successor-version"
```

---

## 🛡️ Rate Limiting

Always return rate limit info in response headers:

```http
X-RateLimit-Limit:     1000
X-RateLimit-Remaining: 847
X-RateLimit-Reset:     1735689600
Retry-After:           60
```

```json
// 429 response body
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Retry after 60 seconds.",
    "retry_after": 60
  }
}
```

**Tier examples:**

| Tier | Limit | Window |
|------|-------|--------|
| Free | 100 req | 15 min |
| Pro | 1,000 req | 15 min |
| Enterprise | 10,000 req | 15 min |

---

## ⚡ Async Operations

For long-running operations, return `202 Accepted` immediately:

```http
POST /api/v1/reports/generate
→ 202 Accepted

{
  "job_id": "job_abc123",
  "status": "queued",
  "status_url": "/api/v1/jobs/job_abc123",
  "estimated_seconds": 30
}
```

Client polls or uses webhook:

```http
GET /api/v1/jobs/job_abc123
→ 200 OK

{
  "job_id": "job_abc123",
  "status": "completed",
  "result_url": "/api/v1/reports/rpt_xyz789"
}
```

> See [Async Processing & Queues](./04-async-processing-queues.md) for queue patterns.

---

## 🧾 Request / Response Implementation

Examples use **FastAPI** (recommended) with a Django REST Framework equivalent where patterns differ.

### FastAPI

```python
from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import Optional
import math

app = FastAPI()

# --- Schemas (Pydantic handles validation automatically) ---

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: str

class PaginationMeta(BaseModel):
    total: int
    page: int
    per_page: int
    pages: int

# --- Response helpers ---

def paginated_response(items: list, total: int, page: int, per_page: int):
    return {
        "data": items,
        "meta": {
            "total": total,
            "page": page,
            "per_page": per_page,
            "pages": math.ceil(total / per_page)
        }
    }

# FastAPI uses exception handlers for consistent error shapes
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.headers.get("X-Error-Code", "HTTP_ERROR"),
                "message": exc.detail,
                "request_id": request.headers.get("X-Request-ID", "unknown")
            }
        }
    )

# --- Endpoints ---

@app.get("/api/v1/users/{user_id}", response_model=dict)
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)  # e.g. Tortoise ORM / SQLAlchemy
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found",
            headers={"X-Error-Code": "NOT_FOUND"}
        )
    return {"data": UserResponse.from_orm(user)}

@app.post("/api/v1/users", status_code=201)
async def create_user(payload: UserCreate):
    # Pydantic already validated payload — no manual validation needed
    user = await User.create(**payload.dict())
    return {"data": UserResponse.from_orm(user)}

@app.get("/api/v1/posts")
async def list_posts(
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=20, ge=1, le=100),  # Max enforced here
    status: Optional[str] = None,
    sort: Optional[str] = "-created_at",
):
    query = Post.filter(status=status) if status else Post.all()
    total = await query.count()
    posts = await query.offset((page - 1) * per_page).limit(per_page)
    return paginated_response([p.dict() for p in posts], total, page, per_page)
```

### Django REST Framework equivalent

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.pagination import PageNumberPagination

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "created_at"]

class StandardPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = "per_page"

    def get_paginated_response(self, data):
        return Response({
            "data": data,
            "meta": {
                "total": self.page.paginator.count,
                "page": self.page.number,
                "per_page": self.get_page_size(self.request),
                "pages": self.page.paginator.num_pages,
            }
        })

class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": {"code": "NOT_FOUND", "message": f"User {user_id} not found"}},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({"data": UserSerializer(user).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": {"code": "VALIDATION_ERROR", "message": "Validation failed",
                           "details": serializer.errors}},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = serializer.save()
        return Response({"data": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
```

---

## 📋 Idempotency Keys

For non-idempotent operations (POST), support an `Idempotency-Key` header:

```http
POST /api/v1/payments
Idempotency-Key: idem_7f3kd92abc

{ "amount": 5000, "currency": "USD" }
```

```python
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import json

class IdempotencyMiddleware(BaseHTTPMiddleware):
    """Replay cached response for duplicate requests with same Idempotency-Key"""

    async def dispatch(self, request: Request, call_next):
        key = request.headers.get("Idempotency-Key")

        if key and request.method == "POST":
            cached = redis_client.get(f"idempotency:{key}")
            if cached:
                payload = json.loads(cached)
                return Response(
                    content=json.dumps(payload["body"]),
                    status_code=payload["status_code"],
                    media_type="application/json"
                )

        response = await call_next(request)

        if key and request.method == "POST":
            body = b""
            async for chunk in response.body_iterator:
                body += chunk
            redis_client.setex(
                f"idempotency:{key}",
                86400,  # 24h TTL
                json.dumps({"status_code": response.status_code, "body": json.loads(body)})
            )
            return Response(content=body, status_code=response.status_code,
                            media_type="application/json")

        return response

app.add_middleware(IdempotencyMiddleware)
```

> Critical for payments, email sends, and anything where duplicate requests cause harm.

---

## 🏷️ Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| URLs | `kebab-case` | `/blog-posts` |
| JSON keys | `snake_case` | `"created_at"` |
| Error codes | `SCREAMING_SNAKE_CASE` | `"NOT_FOUND"` |
| Dates | ISO 8601 UTC | `"2025-01-15T10:30:00Z"` |
| IDs | String (not int in JSON) | `"id": "usr_123"` |
| Booleans | Positive framing | `"is_active"` not `"is_disabled"` |

> **Use string IDs** in JSON responses — integer IDs above 2^53 lose precision in JavaScript.

---

## 🔗 Related Docs

- Slow endpoints? → [Caching Strategies](./01-caching-strategies.md)
- Long-running operations? → [Async Processing & Queues](./04-async-processing-queues.md)
- Monitoring API health? → [Monitoring & Observability](./06-monitoring-observability.md)

---

## 💡 Quick Reference

```
Problem: Inconsistent error shapes across endpoints
→ Solution: Centralised api_error() wrapper

Problem: Clients breaking on new fields
→ Solution: Additive-only changes; never remove fields

Problem: Duplicate POST requests causing double-charges
→ Solution: Idempotency-Key header + Redis deduplication

Problem: Slow paginated queries at high offsets
→ Solution: Switch to cursor-based pagination

Problem: Long-running requests timing out
→ Solution: Return 202 Accepted + poll job endpoint
```

---

*Last updated: 2026*