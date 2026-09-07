class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={} #build hashmap to store seen nums

        for x in range(len(nums)):
            diff = target-nums[x]

            if diff in seen:
                return [seen[diff],x]
            
            seen[nums[x]]=x