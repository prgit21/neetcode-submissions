class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #tarfet = nums[i] +nums [j]
        #use 2ptr

        #brute force is -> start at index, compute every possible combination for triplet across every index and then move first peg index
        #optimal -> se 2 ptr
        #time and space of on2 and o1
        #nums[i]=nums[j]+nums[k]
        #peg nums i and iterate only forwards, allow ptr to move in l-r direction , follow pointers i.e
        #array needs to be sorted
        #apply 2 sum logic while sliding through array is base concept innit?
        
        nums.sort()
        res=[]

        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1

            if i>0 and nums[i]==nums[i-1]:
                continue

            while l<r:
                sum=nums[i]+nums[l]+nums[r]

                if sum <0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while (l<r) and nums[l]==nums[l-1] :
                        l+=1
                
                    
        return res