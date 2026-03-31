class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maxFreq=0
        best=0
        
        l=0

        for r in range(len(s)):
            # find count of window element
            ch=s[r]
            count[ch]= 1+count.get(ch,0)
            # ?after count update max freq

            maxFreq=max(maxFreq,count[ch])

            # force invariant 
            while(r-l+1) -maxFreq >k:
                # remove the left ch and count from window
                left_ch=s[l]
                count[left_ch]-=1
                l+=1
            
            best=max(r-l+1,best)
        return best