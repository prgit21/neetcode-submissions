class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute -> sum every element seen in path , except itself, this is 2 pass so o n pow2
        # optimal ->compute preffix and sufix and then divide it

        n = len (nums)
        pref=suf=1
        res=[1]*n

        for i in range(n):
            res[i]=pref
            pref*=nums[i]

        for i in range(n-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]
        return res