# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = sort_list = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                sort_list.next = list1
                list1 = list1.next
                sort_list = sort_list.next
            else:
                sort_list.next = list2
                list2 = list2.next
                sort_list = sort_list.next
        if list1:
            sort_list.next = list1
        elif list2:
            sort_list.next = list2
        return head.next
        
if __name__ == '__main__':
    l1 = [1,2,4]
    list1 = cur1 = ListNode(l1[0])
    for ele in l1[1:]:
        cur1.next = ListNode(ele)
        cur1 = cur1.next

    l2 = [1,3,4]
    list2 = cur2 = ListNode(l2[0])
    for ele in l2[1:]:
        cur2.next = ListNode(ele)
        cur2 = cur2.next
                    
    s = Solution()
    merge_two_list = s.mergeTwoLists(list1, list2)
    while merge_two_list:
        print(merge_two_list.val)
        merge_two_list = merge_two_list.next