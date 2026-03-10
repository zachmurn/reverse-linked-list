# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # initialize pointers first 

        while curr: #keep going till the end of the list / while curr is not null
            nxt = curr.next # temp variable 
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev
        
