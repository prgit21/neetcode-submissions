class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can use 2 pointers
        #can store occurence of each character and compare them 
        #create a dict to store count of each letter and compare the 2 

        if len(s)!=len(t):
            return False

        countS={}
        countT={}

        for idx in range(len(s)):
            # increment count of every char in s in dict 
            # increment count of every char in t in dict
            
            countS[s[idx]]=1+countS.get(s[idx],0)

            countT[t[idx]]=1+countT.get(t[idx],0)

        return countS==countT
        