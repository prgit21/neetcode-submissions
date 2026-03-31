class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[0]*n
        suff=[0]*n
        res=[0]*n

        pref[0]=suff[n-1]=1

        for _ in range(1,n):
            pref[_] = nums[_-1]*pref[_-1]
        
        for _ in range(n-2,-1,-1):
            suff[_]=nums[_+1]*suff[_+1]
        
        for i in range(n):
            res[i]=pref[i]*suff[i]
        
        return res

        