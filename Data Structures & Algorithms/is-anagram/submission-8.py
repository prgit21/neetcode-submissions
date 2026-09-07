class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can use 2 pointers
        #can store occurence of each character and compare them 
        #create a dict to store count of each letter and compare the 2 

        if len(s)!=len(t):
            return False

        countS={}
        countT={}

        for i in range(len(s)):
            # increment count of every char in s in dict 
            # increment count of every char in t in dict
            
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]]=1+ countT.get(t[i],0)

        return countS==countT
        