class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        #binary search-> we need to find minimal rate at which we can eat abanans under h threshold
        #we can eat min 1 banana an hor
        l=1
        r=max(piles)

        def num_banana(k):
            #method to see total hours taken at this threshhold
            total=0
            for banana in piles:
                total+=math.ceil(banana/k)
            return total

        while l<r:
            #we need to see if at the current rate we can finish pile in < h hrs
            #need to compute a mid value to have effeceient search
            mid=l+(r-l)//2

            if num_banana(mid) <= h:
                #if at this rate of eating abanans can we stay under threshold
                #if yes then we want to move downward
                r=mid
            else:
                l=mid+1
        return l
                


        