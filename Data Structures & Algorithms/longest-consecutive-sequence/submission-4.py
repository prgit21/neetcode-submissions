class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  invariant -> if nums i-1 doesnt exist in a numset then it is a beginning val
        numset=set(nums)
        best=0

        for n in numset:
            if n-1 not in numset:
                length=0
                while(n+length) in numset:
                    length+=1
                    best=max(length,best)
        return best