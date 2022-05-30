# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        tmp = 1
        if count == n:
            head = head.next
        else:
            while curr:
                if tmp == (count-n):
                    curr.next = curr.next.next
                    break
                curr = curr.next
                tmp += 1
        return head