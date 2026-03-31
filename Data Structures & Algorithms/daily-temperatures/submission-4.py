class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack to store indices
        #check if day at top of stack is warmer than last unresolved day
        #if todays temp > temp at top of stack 

        #scan whole array
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                res[prev]=i-prev
            stack.append(i)
        return res