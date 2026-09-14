class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force-> process every element from its existing index oneat a tome to find greatest value
        #optimal-> use stack; initialise an array of 0's to fill in 

        #process every temperature in stack
        #when at index 0, look ahead and count index to next warmest day, append to stack
        #then pop stack one at a time to fill in res arr

        res=[0]*len(temperatures)        
        stack=[]

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                #fill in compute logic
                prev=stack.pop()
                res[prev]=i-prev

            stack.append(i)
        
        return res
