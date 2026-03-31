class Solution:
    def isPalindrome(self, s: str) -> bool:


        #use 2 ptr, check if l<r and in that range iterate over every element 
        #if l<r and not akphanum more left
        #if r>l and not alphanum shirnk right
        #compare lower case to botj 
        #return
    

        l,r=0,len(s)-1
        while l<r:

            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
    
    
    def alphanum(self,c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9') 
            
        )