class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  invariant -> if nums i-1 doesnt exist in a numset then it is a beginning val
        numset= set(nums)
        best=0

        for n in nums:
            leng=0
            if (n-1) not in numset:               #it is a beginning seq
                while(n+leng) in numset:
                    leng+=1
                    best=max(leng,best)
        return best