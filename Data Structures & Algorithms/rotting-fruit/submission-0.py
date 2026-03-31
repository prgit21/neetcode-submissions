class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # invariant-> process 2, and convert its neighbors to 2 at the end of each cycle
        #enqueu the new 2s and repeat iteratively
        #state -> at every single level of iteration update minute
        #use fresh to see what remains but dk how to use fresh rn

        q=deque()
        fresh=0
        rows,cols=len(grid),len(grid[0])
        dirs=[(-1,0),(0,-1),(1,0),(0,1)]
        minutes=0

        # parse all elems
        for r in range (rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        while q and fresh>0:
            k=len(q)
            for _ in range(k):
                # pop indices and move in all directions
                r,c=q.popleft()
                for dr , dc in dirs:
                    nr,nc=dr+r,dc+c

                    if 0<=nr <rows and 0 <=nc < cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            minutes+=1
        
        return minutes if fresh ==0 else -1