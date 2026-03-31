class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need to sort the input list in closest order to the origin
        #find distance of each element in input array, and arrange it based on distance from centre
        #brute force -> every input element, removed from list compute distance and use a hashmap to
        #store distance of point corresponding to indice
        #sort hashmap based on distance and return inp[indice] of k elements
        #optimal -> use max heap of size k, if you find a distance shorter than the max heap element replace it

        heap=[]     #store -dist and x,y

        for x,y in points:
            #scan and compute dist
            dist=x*x+y*y
            heapq.heappush(heap,(-dist,x,y))
            #pushed into heap, now maintain only max k len of heap and remove longest distance

            if len(heap) >k:
                heapq.heappop(heap)
            res=[]

            for item in heap:
                res.append([item[1],item[2]])
        return res