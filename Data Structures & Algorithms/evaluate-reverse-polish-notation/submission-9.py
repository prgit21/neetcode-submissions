class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use stacks
        #for inp in tokens: 
        # if inp is number add to stack
        # if input is +,-,/ or * then pop stack and expose to logic
        #use switch case based on arithmetic token to do precise math

        stack =[]
        for item in tokens:
            if item.lstrip('-').isdigit():           #input is a digit
                stack.append(int(item))
            else:                
                b=stack.pop()
                a=stack.pop()

                match item:

                    case '+':
                        stack.append(a+b)

                    case '-' :
                        stack.append(a-b)

                    case '/' :
                        stack.append(int(a/b))

                    case'*':
                        stack.append(a*b)
                        
            
        return stack[-1]