class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over whole board for r and 
        # check if rows and cols exist and then initalise then

        def dfs(r,c):
            # returns nothing, just checks adjacent nodes for 1 , converts visited 1's to 0
            # check in range
            if r<0 or r>= rows or c< 0 or c>=cols or grid[r][c]=='0':
                return
            
            # convert seen r,c to 0
            grid[r][c]='0'

            # now need to move to dfs of parallel board

            for dr,dc in dirs:
                dfs(r+dr,c+dc)

        if not grid or not grid[0]:
            return 0 
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        count=0

        rows,cols=len(grid),len(grid[0])

        #iterate through every row and col on board, and call dfs when you see 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count+=1
                    dfs(r,c)
        return count
        