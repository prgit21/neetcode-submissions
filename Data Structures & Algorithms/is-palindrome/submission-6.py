class Solution:
    def isPalindrome(self, s: str) -> bool:
        #invariant -> set 2 pointers on either end of the string, ignore non alphanum chars
        #if both ptrs are equal till they see each other then plaindrome
        #time o(n) and space nothing extra o(n)
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            r-=1
            l+=1
        return True