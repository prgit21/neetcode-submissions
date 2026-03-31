class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset= set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)      
        return False
        


        #put in hashset
        #check if element exists in current hashset -> return true
        #else add elem to hashset and after iteration exit