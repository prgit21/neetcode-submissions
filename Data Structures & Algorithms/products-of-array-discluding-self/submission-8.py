class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force -> multiply all numbers of array and then divide index element of corresponding index to get res
        #use prefix and suffix for optimal
        # ik its something like find an array of prefix and suffix
        #then multiply the prefix and suffix array to find res

        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        res=[0]*n

        for _ in range(1,n):
            prefix[_]=prefix[_-1]*nums[_-1]

        for _ in range(n-2,-1,-1):
            suffix[_]=suffix[_+1]*nums[_+1]

        for idx in range(n):
            res[idx]=prefix[idx]*suffix[idx]
        return res