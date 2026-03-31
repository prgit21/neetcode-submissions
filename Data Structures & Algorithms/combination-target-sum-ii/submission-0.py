class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #same as combination sum1
        #list order is different, is it just sort and then apply the same combination1 sum logic?
        #if only duplicates are the issue, why is [2,2,4] valid? is it duplicates based on index as well?
        #if the only issue is handling duplicates, we can sort array then do dfs at every index, and if path contains
        #duplicate we just dont append that path to res
        
        path=[]
        res=[]
        def dfs(start,rem):
            
            # need a check over here before appending path.copy to res based on index of elem

            if rem==0:
                #should i implement the duplication check here?
                res.append(path.copy())                
                return
            if rem < 0:
                return 

            for _ in range(start,len(candidates)):
                if _ > start and candidates[_] == candidates[_-1]:
                    continue
                path.append(candidates[_])
                dfs(_+1,rem-candidates[_])
                path.pop()        
        candidates.sort()
        dfs(0,target)
        return res