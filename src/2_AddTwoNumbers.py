# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        self.curr = prehead
        self.carry = 0
        while l1 and l2:
            tmp = l1.val + l2.val + self.carry
            self.carry = tmp // 10
            self.curr.next = ListNode(tmp%10)
            self.curr = self.curr.next
            l1 = l1.next
            l2 = l2.next
            
        def restAppend(l):
            while l:
                tmp = l.val + self.carry
                self.carry = tmp // 10
                self.curr.next = ListNode(tmp%10)
                self.curr = self.curr.next
                l = l.next
        restAppend(l1)
        restAppend(l2)
        
        if self.carry > 0:
            self.curr.next = ListNode(1)            
        
        return prehead.next
                    
                
                
                
            