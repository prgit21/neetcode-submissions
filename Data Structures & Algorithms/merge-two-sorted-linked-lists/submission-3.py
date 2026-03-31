# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummynode
        #set tail 
        #while both lists exist compare their value
        #if list1.val smaller than list2.val append it to dummy list 
        #move ptr fwd
        #append rest of list 
        #return dummy head

        dummy=ListNode()
        tail=dummy
        while list1 and list2:
            if list1.val<list2.val:
                #select list 1 val node and append to dummy
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next #dont overwtie the same one
        
        tail.next= list1 or list2
        return dummy.next