class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #invariant -> 2 uniqe indcies in input sum up to target
        #approach -> use a hashmap to store seen values
        #if diff - seen in nums return the indice

        seen={}

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in seen:
                return [seen[diff],i]
            
            seen[nums[i]]=i

        