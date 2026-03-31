class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #do dfs at every index, for elements of idx > start idx
        #store copy of list path at every stage of dfs
        res=[]
        path=[]
        def dfs(start):
            res.append(path.copy())
            for _ in range(start,len(nums)):
                path.append(nums[_])
                dfs(_+1)
                path.pop()        
        dfs(0)
        return res
