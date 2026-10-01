class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #naive-> find every substring and try replacing max k to find len
        #optimal -> sliding window
        #store frequency of every char being processed using a counter
        #in a given window find the most frequent elem
        #for every non frequent element seen decrement k
        #if k =0 and another non frequent element is seen calc window size
        #push l 
        #ret max global winsow  size

        count=Counter()
        l=0
        r=0
        res=0

        for r in range(len(s)):
            #check if window is valid, else decrement and move l 
            #for window to be valid, number of most un-common elem<=k
            #number of replacements = window size - freq of most common 
            window_size=r-l+1
            count[s[r]]+=1
            freq_common=max(count.values(),default=0)

            if (window_size-freq_common)<=k:
                res=max(res,window_size)
                
            else:
                count[s[l]]-=1
                l+=1
        return res

                





            #process char and take its count and update global window size