class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #use dfs and backtracking
        #store path and append to list res to return p
        #create a used state variable to prevent duplication during recursion
        #backtrack both path and used state to allow reusing of multiple permutations

        res=[]
        path=[]
        used=[False]*len(nums)

        def dfs():

            if len(nums)==len(path):
                res.append(path.copy())
                return 

            for _ in range(len(nums)):
                #used state to ensure we pick only 1 of available in each sub permutation
                if used[_]:
                    continue
                used[_]=True

                path.append(nums[_])
                dfs()
                used[_]=False
                path.pop()

        
        dfs()
        return res