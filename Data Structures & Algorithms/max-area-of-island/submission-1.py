class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we must scan all connected islands , and never scan the same node mroe than once
        #the dfs must return an area after every single scan of connected islands so we can compute max seen so far

        # check if r and c exist
        if not grid or not grid[0]:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        maxArea=0
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        
            # returns area
        def dfs(r,c) -> int:
            # check if in range and processing only unseen nodes
            
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0

            # update seen grid
            grid[r][c]=0

            # move dfs to see if djacent nodes are also islands
            areas = 1
            for dr,dc in dirs:
                areas+=dfs(dr+r,dc+c)
            
            return areas
            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    # trigger dfs and compute max area seen so far
                    area= dfs(r,c)
                    maxArea=max(maxArea,area)
        return maxArea
