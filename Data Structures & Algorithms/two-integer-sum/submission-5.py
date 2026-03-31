class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #assumptions -> one valid solution exists in list, nums can be either +ve or -ve and an empty nums list doesnt exist
        # brute force -> compare everey single index with every other index till we find matching solutiuin o(n pow 2 )time and o (n) space

        #optimsied solution -> use a hashmap to store values you have previously seen, use the array index as key and the value as value
        #hashmap allows effecient lookup of o(n)
        #iterate through list, and compare nums[i] with previously seen elements in hashmap to find target= nums[i]+nums[j]
        # return nums i and j

        seen ={}
        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in seen:
                return [seen[diff],i]
            seen[nums[i]]=i