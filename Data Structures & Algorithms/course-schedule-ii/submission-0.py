class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        done=set()
        visiting=set()
        resorder=[]

        pre=defaultdict(list)

        for course,req in prerequisites:
            pre[course].append(req)
        
        def dfs(c) :
            

            if c in visiting:
                return False
                
            if c in done:
                return True
            
            visiting.add(c)
            for courses in pre[c]:
               ok=dfs(courses)
               if not ok:
                return False
            
            visiting.remove(c)
            done.add(c)
            resorder.append(c)
            return True
            

        
        for crs in range(numCourses):
           ok=dfs(crs)
           if not ok:
            return []
        return resorder
        