class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #invariant -> ensure that you maintain window size - maxFreq elemt count <=k
        #i.e max replacements needed to have window size is lesser than k

        freq={}
        
        l,r=0,0
        maxFreq,res=0,0

        for r in range(len(s)):
            #count freq of elem and decide max freq
            freq[s[r]]=freq.get(s[r],0)+1
            maxFreq=max(maxFreq,freq[s[r]])

            #if window size - maxFreq > max replacement allowed -> shrink
            while ((r-l+1)-maxFreq)>k:
                #shrink
                freq[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            