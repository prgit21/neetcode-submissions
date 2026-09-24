class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #do binary search
        #if element exists, return index 
        #split array into the middle and search either left or right dragment recursi
        #if elem ret idx else -1

        l=0
        r=len(nums)-1

        while l<=r:
            #find middle

            mid=l+(r-l)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                l=mid+1

            elif nums[mid]>target:
                r=mid-1
        return -1