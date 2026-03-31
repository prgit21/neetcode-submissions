class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for x in nums:
            self.add(x)
        

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            # if len of heap less than k, have empty space to add more then heapq it
            heapq.heappush(self.heap,val)

        elif val>self.heap[0]:
            # pop heap from min position 
            heapq.heapreplace(self.heap,val)
        return self.heap[0]

        
