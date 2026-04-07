# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not len(lists): return  # edge case for empty list
        if len(lists) == 1: return lists[0]
        final = lists[0]

        for itemHead in lists[1:]:

            finalHead = final
            curr = temp = ListNode()
            while finalHead and itemHead:
                minVal = min(finalHead.val, itemHead.val)
                if minVal == finalHead.val:
                    finalHead = finalHead.next
                else:
                    itemHead = itemHead.next
                curr.next = ListNode(val=minVal)
                curr = curr.next
            if finalHead:
                curr.next = finalHead
            elif itemHead:
                curr.next = itemHead
            # print(final.val, temp.val, curr.val)
            final = temp.next
        
        return final
        