# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = newHead = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                newHead.next = list1
                list1 = list1.next
            else:
                newHead.next = list2
                list2 = list2.next
            newHead = newHead.next
        if list1:
            newHead.next = list1
        else:
            newHead.next = list2
        return dummy.next
                

            
