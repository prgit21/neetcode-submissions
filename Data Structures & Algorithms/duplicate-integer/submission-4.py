class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()

        for _ in range(len(nums)):
            seen.add(nums[_])
        
        if len(nums)> len(seen):
            return True
        else:
            return False
            
        

        