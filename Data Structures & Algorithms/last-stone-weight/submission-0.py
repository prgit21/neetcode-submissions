class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #simulate max heap
        #pop max heaptwice to find two biggest values
        #if x==y, do nothing, if x<y insert y-x into heap again 
        
        #insert stones array into heap using heapify -> this runs in o(n log n )

        heap=[-s for s in stones]
        #heapify it
        heapq.heapify(heap)    


        while len(heap) >1:
            x=-heapq.heappop(heap)  #biggest
            y=-heapq.heappop(heap)  #2nd biggest

            if x!=y:
                heapq.heappush(heap,-(x-y))

        return -heap[0] if heap else 0