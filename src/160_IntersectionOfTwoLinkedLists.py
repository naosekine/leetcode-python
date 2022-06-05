# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        copyA = headA
        A = {}
        type(id(headA))
        while headA:
            A[id(headA)] = True
            headA = headA.next
        while headB:
            if id(headB) in A:
                return headB
            headB = headB.next