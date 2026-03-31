class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a res list to store number of days after which it is warmer
        #use a stack to store how many days you go before u see the warmer day
        #appendd every day to the stack
        #check if todays temp is warmer than the top of the stack recuraively
        #if you find a warmer day, find the today (idx) and the day which is in stack diff and update res

        stack=[]
        res=[0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                res[j]=i-j
            stack.append(i)
        return res

