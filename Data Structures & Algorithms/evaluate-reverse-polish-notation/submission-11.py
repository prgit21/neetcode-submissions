class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #push to stack if number, if operand pop stack and apply it
        #brute force -> check if 
        stack=[]

        for inp in tokens:
            #need to process all tokens l to r
            #switch case style on the operand

            match inp:
                case '+':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(a+b))
                case '-':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b-a))
                case'*':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b*a))
                case '/':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int((b/a)))
                case _:
                    stack.append(int(inp))
        
        return stack.pop()