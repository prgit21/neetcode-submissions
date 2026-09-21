class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #optimal-> use loop and just return when found lol
        #req-> implement binary search algo

        #binary search -> 
        # find middle, if target < middle increment l ptr else r ptr and then recompute middle every iteration
        #middle = low-high //2

        l=0
        h=len(nums)-1

        while l <= h:
            mid=l+(h-l)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1