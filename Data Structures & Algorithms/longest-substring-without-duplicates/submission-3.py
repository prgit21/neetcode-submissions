class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start with left ptr,and add all elements seen in string till we see a duplicate
        #if we see a duplicate then emoty the set and move the left pointer
        #we want to check duplicates against r ptr and add elements with r pointer 
        #but we want to remove only the first seen duplicate element
        #compute max len every time we 

        l=0
        chars=set()
        count=0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            count=max(count,r-l+1)
        return count