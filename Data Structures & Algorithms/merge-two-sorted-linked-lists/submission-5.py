# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #idea is to merge two sorted linked list
        #maybe pick a dummy head, to handle first and last edge cases
        #and to dummy pick and append list1 or list2 head, move pointer forward on selected one
        #move tail pointer ahead
        #append remaining list 
        #key invariant -> at every point pick the node which has llower value bw l and r list

        dummy=ListNode()
        tail=dummy

        #first check that either lists need to exist

        while list1 and list2:
            #check head of list1 and list2 to pick whats smaller

            if list1.val < list2.val:
                #point smaller node from tail and move ahead list1
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            
            tail =tail.next #have to move the tail pointer also to next node otherwise we keep replacing in same place
        #now need to append remaining of list 1 or list2

        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        
        return dummy.next


