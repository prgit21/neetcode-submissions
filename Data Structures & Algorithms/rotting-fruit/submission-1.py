class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # invariant-> neighbor of rotten turns into rotten with every iteration
        #need to apply bfs

        q=deque()
        fresh=0
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        rows,cols=len(grid),len(grid[0])
        minutes=0

        for r in range(rows):
            for c in range(cols):       #iterate through board
                if grid[r][c]==2:
                    q.append((r,c))     #if rotten append to q for processing
                elif grid[r][c]==1:
                    fresh+=1            #if fresh coun tit
        
        while q and fresh>0:
            lev_size=len(q)
            for _ in range(lev_size):
                # at every level need to rot neighbors
                r,c=q.popleft()
                for dr,dc in dirs:
                    nr=dr+r
                    nc=c+dc

                # move around and check for nbrs
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2        #immediately rot neighbors of rotten and decrement count
                        fresh-=1
                        # append the new rotten neighbors to the rotten q for processing
                        q.append((nr,nc))
            minutes+=1
        
        return minutes if fresh ==0 else -1

