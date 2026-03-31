class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res=[]

        def backtrack(openN,closedN):
            if openN== closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return res

        #empty stack and res array
        #if openN=closedN=n then res.append(".join(stack)")
        #if openN<closedN: ->append "(" backTrack(openN+1,closedN) stack.pop
        #if closedN<openN: -> append ")" backtrack(openN,closedN+1) stack.pop