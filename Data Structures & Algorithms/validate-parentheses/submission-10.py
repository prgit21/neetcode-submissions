class Solution:
    def isValid(self, s: str) -> bool:
        #brute force -> remove valid brackets till none exists, dont quite understand how
        #optimal-> use stack to store valid closing bracke
        #build dict of closed to open key value pairs
        closeToOpen={'}':'{', ']':'[' , ')':'('}
        stack=[]
            
        
        #need to process every input element l - r:
        for char in s:
            #now neew to check if it is closing bracket
            #do this by checking if its valid key
            if char in closeToOpen:
                #now we know its valid opening bracket
                #check if stack is empty and we are tying to

                if not stack or stack[-1]!=closeToOpen[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack

        