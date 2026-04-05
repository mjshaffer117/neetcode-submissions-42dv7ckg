# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]

            left_merged = self.mergeKLists(left)
            right_merged = self.mergeKLists(right)

            return self._mergeHelper(left_merged, right_merged)
    
    def _mergeHelper(self, left, right):
        curr = senNode = ListNode(0)
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        while left:
            curr.next = left
            left = left.next
            curr = curr.next

        while right:
            curr.next = right
            right = right.next
            curr = curr.next

        return senNode.next