

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        #reverse 2nd half
        #interleave merge the first and second

        if not head or not head.next:
            return 

        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse it
        prev=None
        curr=slow.next
        slow.next=None #cut in half
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        left=head
        right=prev
        
        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        return