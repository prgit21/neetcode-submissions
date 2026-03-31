class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #bruteforce -> sort strings and compare character by character
        #assumption -> string is in lower case so no transform needed, mpty string is possible 
        #need help in figuring out time complexity in brute force -> sort + compare time and space is same o(1)          
        #optimal sol -> use hashmap  to count occurence of every single str elem, if count is same return true else false

        if len(s)!=len(t):
            return False

        countT,countS={},{}

        for idx in range(len(s)):
            countT[t[idx]]=1 + countT.get(t[idx],0)
            countS[s[idx]]=1 + countS.get(s[idx],0)
        return countS==countT