class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start with 2 ptrs, on lhs, adjust window sizing as we parse through
        #store parsed window elemtns in hashset
        #if seen again then slide left window

        l=0
        chars=set()
        res=0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            res=max(res,r-l+1)
        return res

