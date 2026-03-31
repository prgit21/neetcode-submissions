class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #need to sort array, and then compare        
        #compare if start of next sub list is < end of current sub list -> merge them as intervals
        #repeat until no sub intrvals are left 
        #return the rest of input as a different list and this merged intervals as one list
        if intervals is None:
            return []

        res=[]
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]

            last_end=res[-1][1]

            if curr_start <=last_end:
                res[-1][1]=max(last_end,curr_end)
            else:
                res.append(intervals[i])
        return res