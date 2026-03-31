class Solution:
    def isValid(self, s: str) -> bool:
        #use a dicrtionary -> map all closed to open
        #append all opening bracket string you see into a stack
        #if u see a close then you want to compare stack top and pop it if it matches otherwsie you ret false
        #if stack is empty return valid
        
        match={'}':'{',']':'[',')':'('}
        stack=[]

        for ch in s:
            if ch in match:     #if it is a key in dict
                # if not stack:
                #     return False
                if not stack or stack[-1]!=match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack