class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def dfs(start_idx):
            res.append(path.copy())
            for _ in range(start_idx,len(nums)):
                path.append(nums[_])
                dfs(_+1)
                path.pop()

        dfs(0)
        return res