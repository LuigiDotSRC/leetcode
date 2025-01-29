from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        ptr, prev = head, None
        while ptr != None:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        return prev