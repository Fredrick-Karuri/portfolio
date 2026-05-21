class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        THE PROBLEM: Reverse a singly linked list so the tail becomes the head

        PATTERN: In-place pointer manipulation (Three-pointer tracking)

        INSIGHT: You cannot just change current.next to point backward without 
        losing the rest of the list. You must store the next node before 
        severing the original link.

        THE PLAN:
        1. Initialize prev pointer to None and curr pointer to head
        2. Loop through the list while curr is not None
        3. Save the next node in a temporary variable (nxt = curr.next)
        4. Flip the pointer backward (curr.next = prev)
        5. Move prev to curr and curr to nxt to advance the window
        6. Return prev as the new head of the reversed list

        Example: head = 1 -> 2 -> 3 -> None
        - Step 1: curr=1, nxt=2 -> 1 points to None -> prev=1, curr=2
        - Step 2: curr=2, nxt=3 -> 2 points to 1    -> prev=2, curr=3
        - Step 3: curr=3, nxt=None -> 3 points to 2 -> prev=3, curr=None
        Result: 3 -> 2 -> 1 -> None

        TIME: O(n)
        SPACE: O(1)
        """
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # Save next node
            curr.next = prev  # Reverse link
            prev = curr      # Move prev forward
            curr = nxt       # Move curr forward

        return prev
