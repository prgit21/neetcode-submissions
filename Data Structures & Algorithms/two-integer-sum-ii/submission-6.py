class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use 2 ptr, start from end of window
        #sum=char index [r] elem index r 
        #if sum < target move left otherwise move right

        l,r=0,(len(numbers)-1)

        while l<r:
            sums=numbers[l]+numbers[r]

            if sums<target:
                l+=1
            elif sums > target:
                r-=1
            elif sums==target:
                return[l+1,r+1]
