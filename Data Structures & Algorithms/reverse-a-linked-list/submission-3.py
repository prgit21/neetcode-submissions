# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #naive-> convert to array and flip & return 
        #optimal-> linked list
        #move head to end +1 and current to point backwards

        prev=None
        cur=head

        while cur:
            #save ahead
            #point backward
            #move both pointers
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

            
        return prev


        
        


