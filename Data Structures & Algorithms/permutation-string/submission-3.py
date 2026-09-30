class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force-> take size of substring and at every index check if any valid permutation of the same exists on pow 2
        #optimal -> sliding window
        
        #store frequency of s1 and use slidingn window to select a substring of s2
        #compare the substring frequency map with s1 frequency, if no match ret false
        

        count_s1=Counter(s1)
        freq_sub=Counter()

        l=0
        r=0

        for r in range(len(s2)):
            
            #build frequency map of substring
            freq_sub.update(s2[r])

            #manage window size
            if (r-l+1)>len(s1):
                freq_sub[s2[l]]-=1
                l+=1
            
            #check if substring is same value as s1
            if count_s1==freq_sub:
                return True

        return False


            


            


        