class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #invariant -> use 2 pointers and shrinking window, compare height of l and r, move constraint and store 
        #global max vol of water till window valid

        l,r=0,len(heights)-1
        area,maxW=0,0

        while l<r:
            #first compute vol, then adjust windows, and update global state
            area=(r-l)*(min(heights[l],heights[r]))
            maxW=max(area,maxW)
            #conditions for pointer to move
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxW
            