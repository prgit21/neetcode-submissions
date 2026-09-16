class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force-> string reverse and compare -> o(n) extra space
        #optimal -> have an is alnum check
        #if !alnum then move pointer inward
        #if alnum then compare lhs with rhs pointer
        #if r>l then ret palindrome or eaely exist

        l=0
        r=(len(s)-1)
        

        while r>l:
            #while lhs and rhs is not alnum keep comparing and pushing 
            #while it is not alnum we must keep moving till its alnum

            while not s[l].isalnum() and  l<r:
                l+=1
            while not s[r].isalnum() and  l<r:
                r-=1

            while s[l].isalnum() and s[r].isalnum() and  l<r:
                if not s[l].lower()==s[r].lower():
                    return False
                else:                    
                    r-=1
                    l+=1
            
            #make sure we move r and l after every iteration 
            # #i feel this isnt needed then it will just skip
            # l+=1
            # r-=1
        return True