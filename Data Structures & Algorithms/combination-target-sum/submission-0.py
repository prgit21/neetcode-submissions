class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]

        def dfs(start,rem):
            if rem ==0:
                res.append(path.copy())            
                return 
            if rem <0:
                return
            for _ in range(start,len(nums)):
                path.append(nums[_])
                dfs(_,rem-nums[_])
                path.pop()
        
        dfs(0,target)
        return res