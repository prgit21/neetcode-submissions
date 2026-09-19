class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force-> calculate all possivle combinations by stopping at every index and keep absolute maximum 

        #optimal-> use two pointers, l and r-1
        #calculate volume of water for every iteration and store globalm ax
        #if h[l]<=h[r]:l++ else r--
        #do while l<r:

        l=0
        r=len(heights)-1
        maxWater=0

        while l<r:            
            #calculate amount of water per iteration, and store max 
            area=(min(heights[l],heights[r])*(r-l))
            maxWater=max(maxWater,area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxWater
