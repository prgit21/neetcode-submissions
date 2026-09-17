class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #naive soln is to just use hashmap and arrays but thats extra space
        #for o(1) space just use 2 pointers, init l and r ptr
        #if sum < target move lptr otherwsie right ptr till we find sum
        # dont need to evaluate for when no soln cus always has soln
        #use 1 based indexing 

        l=0
        r=len(numbers)-1

        while l<r:
            #evaluate the value of sum every time before we move pointer
            sums=numbers[l]+numbers[r]
            if target==sums:
                return [(l+1),(r+1)]

            if sums<target:
                l+=1

            elif sums>target:
                r-=1
            
