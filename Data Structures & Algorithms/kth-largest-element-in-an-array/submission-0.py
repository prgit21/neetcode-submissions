class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #brute force -> sort elements in array, return kth element, o nlogn time 
        #optimal -> use min heap, pop k times and return heap[0] ( max heap for largest)
        #assume k is +ve and input always exosts, -ve and +ve values possible in inp stream

        heap=[-num for num in nums]
        heapq.heapify(heap)

        for _ in range (k-1):
            heapq.heappop(heap)
        
        return - heapq.heappop(heap)