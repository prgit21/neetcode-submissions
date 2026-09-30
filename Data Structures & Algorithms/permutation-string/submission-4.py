class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force-> take size of substring and at every index check if any valid permutation of the same exists on pow 2
        #optimal -> sliding window
        
        #store frequency of s1 and use slidingn window to select a substring of s2
        #compare the substring frequency map with s1 frequency, if no match ret false
        #answer is recorded when window is valid

        l=0
        r=0
        counts1=Counter(s1)
        counts2=Counter()

        for r in range(len(s2)):
            #we need to record answer when window is valid
            #  add to the counter, check its size and manage valid window            
            # then we check if its valid answer
            # a dd to counter
            counts2[s2[r]]+=1

            #check valid size
            if (r-l+1)>len(s1):
                counts2[s2[l]]-=1
                l+=1
            
            # check valid answer

            if counts1==counts2:
                return True
        return False

        

        