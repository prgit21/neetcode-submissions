# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr:
            #save ahead
            nxt=curr.next
            #flip
            curr.next=prev
            #advance
            prev=curr
            curr=nxt
        return prev