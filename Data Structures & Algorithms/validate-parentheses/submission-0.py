class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={"}":"{", 
        ")":"(" ,
        "]":"["
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        #init empty stack and create bracket map
        #for c in s and c in closeToOpen
        #if stack and stack[-1] == present in closeToOpen[c] -> pop stack otherwise false
        #if c not in closeToOpen append stack
        #return true if stack empty

        