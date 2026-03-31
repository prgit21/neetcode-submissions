class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        res=0

        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res

        #set charset to have ready count of what is repeated
        #init l pos and res
        
        #for r in range of len of str
        #check while s[r] is in charset, remove from left most position ( slide window)
        #update l pts of sliding window
        #after removing dups, add s[r] to charset and update res =max(res,r-l+1)
            

        