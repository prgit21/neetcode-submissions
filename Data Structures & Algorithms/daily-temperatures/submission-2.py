class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a res list to store number of days after which it is warmer
        #use a stack to store how many days you go before u see the warmer day
        #appendd every day to the stack
        #check if todays temp is warmer than the top of the stack recuraively
        #if you find a warmer day, find the today (idx) and the day which is in stack diff and update res

        stack=[]        #waiting days
        res=[0] * len(temperatures)

        for _ in range(len(temperatures)):
            #passes through all days and ensures we scan whole list
            while stack and temperatures[_]> temperatures[stack[-1]]:
                # while todays temp watmer than whatever day stack i s on
                # j = the day the stack is on today, pops the day on which the stack is there
                j=stack.pop()
                res[j]= _ - j                            
            stack.append(_)
        return res
        