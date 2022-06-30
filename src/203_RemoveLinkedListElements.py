# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = head
        ans = []
        prehead = anslist = ListNode(-1)
        while prev:
            if prev.val != val:
                ans.append(prev)
            prev = prev.next
        
        for node in ans:
            anslist.next = node
            anslist = anslist.next
        anslist.next = None
        return prehead.next