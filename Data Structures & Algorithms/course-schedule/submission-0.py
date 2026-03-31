class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # goal is to check if there is a cycle
        #invariant -> if dfs (c) item is already seen, cycle exists. store c in visiting state and then move to done
        # if dfc(c) in done, then cycle
        # need adjacency list to be able to traverse the graph effeciently

        pre=defaultdict(list)
        for course,req in prerequisites:
            pre[course].append(req)
        
        visiting=set()
        done=set()

        def dfs(c):
            # check if visiting now
            if c in visiting:
                return False        #cycle seen
            if c in done:
                return True         #already validated and proven safe
            
            # append c to visitng path
            visiting.add(c)

            # check if req of course has cycle
            for req in pre[c]:
                ok=dfs(req)
                if not ok:
                    return False
            visiting.remove(c)
            done.add(c)

            return True
                
        
        
        
        for crs in range(numCourses):
            ok =dfs(crs)
            if not ok:
                return False
        return True
        
