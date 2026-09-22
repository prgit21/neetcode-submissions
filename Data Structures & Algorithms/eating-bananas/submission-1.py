class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #brute force-> start with 1,and then increment number of hours of k per stack and pick lowest valid asnwer
        #brute -> for eating speed k process one pile in one unit of time
        #repeat till you have lowest value 
        #o n*m time 
        #optimal-> use binary search dk how         
        # binary search
        #write a helper to find out if k can process piles within target h
        #use binary search to find the lowest k 

        def find_k_helper(k):
            #at this value of k can koko eat entire stack
            #return total number of hours which is needed at this k             
            total=0

            for banana in piles:
                #process every banana in pile
                #how many hours does it take for this value k to process one pile
                total+=math.ceil(banana/k)
            return total            

        low=1
        high=max(piles)

        while low<high:
            #binary search is to find min value of k 
            mid=low+(high-low)//2
            if find_k_helper(mid)<=h:
                #can technically do mid+1 as well
                high=mid
            else:
                #technically even can just increment l by 1 itll
                #get the job done bbut maybe time complextiy bleeds
                low=mid+1            
        return low




