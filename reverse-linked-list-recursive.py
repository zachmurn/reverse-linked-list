# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive: T O(n), M O(n)

        if not head:
            return None # if the head is null, return null
        
        newHead = head
        if head.next: #if there's still a sub-problem 
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None 

        return newHead
