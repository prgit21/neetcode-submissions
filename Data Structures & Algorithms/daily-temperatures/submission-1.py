class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create a stack to store monotonic decreasing values
        #for temperatures: -> parse array and push all elements into stack that 
        #are lesser than the previous value
        #when elem bigger than previous found, pop top untill descending order restored
        #after pop, use indice of stack to calc distance and store in array pos
        # for all elem left in stack populate 0

        stack=[]
        res=[0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                _,stackIndex=stack.pop()
                res[stackIndex]=(idx-stackIndex)
            stack.append([temp,idx])
                
            
            
        return res
            
            
            
        