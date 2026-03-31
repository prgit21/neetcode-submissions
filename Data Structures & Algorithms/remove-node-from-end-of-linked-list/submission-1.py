# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # core idea -> remove a node at pos n and return list
        #task -> move to before nth node and then do ptr manipilation to ensure .next.next simple
        #invariant -> use a fast and slow ptr,maintain gap of n bw fast and slow
        
        dummy=ListNode(0)
        dummy.next=head

        slow=fast=dummy

        for i in range(n):
            fast=fast.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next

        return dummy.next