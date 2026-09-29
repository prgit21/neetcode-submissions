class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force-> find every permutation of string possible starting at initial index store it and then splice and find the longest substring 
        #optimal-> use sliding window
        #start the sliding window, at every movement of l and r store/remove the 
        #char from dict , at every iter store len of window and a global max
        #ret global max

        l=0    
        seen=set()
        maX=0

        for r in range(len(s)):
            #while s[r] is already in seen
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            # a dd s[r]
            seen.add(s[r])

            #compute best
            maX=max(maX,((r-l)+1))
        return maX

            