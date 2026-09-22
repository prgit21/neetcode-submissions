class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def find_k(k):
            total=0
            
            for banana in piles:
                total+=math.ceil(banana/k)
            return total

        low=1
        high=max(piles)

        while low<high:
            # need to do binary search over 1:high
            mid=low+(high-low)//2

            if find_k(mid)<=h:
                high=mid
            else:
                low=mid+1
        return low