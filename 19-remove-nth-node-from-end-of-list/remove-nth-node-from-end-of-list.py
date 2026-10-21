# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move fast pointer n + 1 steps ahead so that the gap between fast and slow is n
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # Skip the target node
        slow.next = slow.next.next
        
        return dummy.next