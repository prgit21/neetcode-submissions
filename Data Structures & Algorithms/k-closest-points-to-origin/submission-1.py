class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #brute force -> ensure that we compute distance of all points, store them as a tuple with point and distance 
        #sort based on distance, and return last k relevant o nlog n and o n

        #optimal -> max heap, maintain size of k, and pop when exceeding it

        res=[]
        heap=[]     #store dict , x,y

        for x,y in points:
            #scan and find dist
            dist=x*x+y*y
            heapq.heappush(heap,(-dist,x,y))

            if len(heap)>k:
                heapq.heappop(heap)

        for unpack in heap:
            res.append([unpack[1],unpack[2]])
        return res