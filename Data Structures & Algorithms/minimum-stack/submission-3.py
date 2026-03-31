class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #check if minstack not exist then append, otherwise peek top of minStack, if minstack top < stack top append
        if not self.mstack:
            self.mstack.append(val)
        elif self.stack[-1]<self.mstack[-1]:
            self.mstack.append(val)
        elif val==self.mstack[-1]:
            self.mstack.append(val)
            

        

    def pop(self) -> None:
        #if stack nd stack top nd minstack top == then pop noth otherwise just minstack
        if self.stack[-1] == self.mstack[-1]:
            self.stack.pop()
            self.mstack.pop()
        else:
            self.stack.pop()
            
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return []

        

    def getMin(self) -> int:
        if self.mstack:
            return self.mstack[-1]
        else:
            return []

        
