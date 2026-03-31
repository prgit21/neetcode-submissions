class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None:
            return []
        res=[]

        intervals.sort(key=lambda x:x[0])
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]
            
            last_end=res[-1][1]
            
            if curr_start <= last_end:
                res[-1][1]= max(curr_end,last_end)
            else:
                res.append(intervals[i])
        return res


        