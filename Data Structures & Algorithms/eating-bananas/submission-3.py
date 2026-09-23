class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def find_k(k):
            #return total number of hours at this value of k 
            total=0
            for banana in piles:
                total+=math.ceil(banana/k)
            return total

        l=1
        high=max(piles)

        while l<high:
            middle=l+(high-l)//2

            if find_k(middle)<=h:
                #if total number of hours are less than equal 
                #then its valid anyway, try finding a smaller value
                #do binary search over the number of k per pile
                high=middle
            else:
                l=middle+1
        return l

        
