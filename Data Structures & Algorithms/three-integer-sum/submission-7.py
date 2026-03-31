class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use.2 ptr
        #run it n times, ensure that l and r are setup per loop- > need to resrt l and r and ensure it runs per step 
        #compute sum and move ptr acc
        #after finding sol move ptr to avoid dupe and then add a check to prevent subsequent repeats
        
        nums.sort()
        res=[]

        for i in range(len(nums)):
            # we want to scan from left to right and anchor one of the indices and only move forwards
            l=i+1
            r=len(nums)-1

            if i>0 and nums[i]==nums[i-1]:
                    continue
            
            while l<r:
                # calculate sum
                msum=nums[i]+nums[l]+nums[r]

                if msum<0:
                    l+=1
                elif msum>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res


