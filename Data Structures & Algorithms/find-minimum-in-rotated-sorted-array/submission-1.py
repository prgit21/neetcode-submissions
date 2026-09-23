class Solution:
    def findMin(self, nums: List[int]) -> int:
        #trivial-> use min 
        #use binary search and store global min 

        l=0
        h=len(nums)-1

        while l<h:
            middle = l+(h-l)//2
            # keep doing binary search and throw away 
            #but how can you do binary search on non sorted array
            #2 sorted arrays formed by rotation 
            #bamboozled, give hints 

            if nums[h]<nums[middle]:
                #then smallest val is in rhs 
                l=middle+1
            else:
                h=middle
        return nums[l]
