class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #ok serious approach 
        #brute force - > sort list and if idx[i]==idx[i-1] return duplicates, or compare every idx to val uses extra space 
        #optimal -> use a hashset to check dupes
        #assumption ums list has values, is not empty
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        