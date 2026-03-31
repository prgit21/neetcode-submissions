class MinStack:
        #invariant => use stack, 2 of them
        #one to maintain min and one regular one

    def __init__(self):
        #init 2 stacks
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        #push to both stack if stack empty, 
        #if min top is < val push to min stack
        #otherwise just push to stack
        if len(self.stack)==0:
            self.stack.append(val)
            self.minStack.append(val)
        elif val<=self.minStack[-1]:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
        

    def pop(self) -> None:
        #pop stack, if stack val == minVal top then pop minSrack
        if self.stack[-1]<=self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else:
            self.stack.pop()

        

    def top(self) -> int:
        #peek topp
        return self.stack[-1]
        

    def getMin(self) -> int:
        #return top of minstack
        return self.minStack[-1]
        
