# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

# another solution    
#         curr = head
#         prev = None
#         while curr:
#             next_tmp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_tmp
        
#         return prev