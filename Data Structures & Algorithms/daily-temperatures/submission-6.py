class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force-> stop at every index and calculate how many days till next warmest -> on2
        #optimal -> use a monotonic decreasing stack to find when next warmest day could occur in input


        res=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                #pop stack compute distance and append to res based on index
                previous_day=stack.pop()
                res[previous_day]=i-previous_day

            stack.append(i)

        return res