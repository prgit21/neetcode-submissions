class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use a dict or set to store operators
        #if operator -> then switch case
        #else append to stack

        stack=[]
        opp={'+','-','/','*'}

        for inp in tokens:                  
            if inp in opp:                
                match inp:
                    case '+':
                        a,b=stack.pop(),stack.pop()
                        stack.append( a+b)
                    case  '-':
                        a,b=stack.pop(),stack.pop()
                        stack.append( b-a)
                    case  '/':
                        a,b=stack.pop(),stack.pop()
                        stack.append(int(b/a))
                    case  '*':
                        a,b=stack.pop(),stack.pop()
                        stack.append(a*b)
            else:
                stack.append(int(inp))
        
        return stack[-1]
                
            
