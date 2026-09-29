class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #h -> max hours
        #k -> rate of eat
        #if< k no new pile
        #ret min integer k 
        #brute force-> pin at index, calculate 1-max pile how many is minimum, store gloval min
        #optimal-> use binary search
        #do binary search over max possible k value

        l=1
        r=max(piles)

        def can_eat(k):
            total=0
            for banana in piles:
                total+=math.ceil(banana/k)
            return total

        while l<r:
            mid=l+(r-l)//2
            
            # if you can complete k bananas under h time then throw away right
            if can_eat(mid) <=h:
                r=mid
            else:
                l=mid+1
        
        return l