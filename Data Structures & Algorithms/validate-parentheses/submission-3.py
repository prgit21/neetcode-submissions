class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        #store opening bracket in stack
        #check if closing bracket matches with stack-1 -> true else false
        # check if string empty

        stack=[]
        validBrack={'}':'{',']':'[',')':'('}


        for c in s:
            if c in validBrack:
                if stack and stack[-1]==validBrack[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False