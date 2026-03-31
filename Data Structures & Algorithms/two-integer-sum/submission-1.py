class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}

        for i, n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        

        #init map of prev elem
        #enum through nums 
        #diff=target-n and if diff in prev map return index