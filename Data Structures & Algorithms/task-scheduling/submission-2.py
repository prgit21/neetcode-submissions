class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #approach-> at every cpu cycle process element with highest frequency
        #that is not in coooldown

        if n==0:
            return len(tasks)
        cooldown=deque()
        freq=Counter(tasks)
        heap=[ -count for count in freq.values()]
        heapq.heapify(heap)
        time=0

        while cooldown or heap:
            #scan nd sim when heap or valid elems exist
            time+=1
            while cooldown and cooldown[0][0]<=time:                
                # pop from cooldown and append all valid to heap
                _,count=cooldown.popleft()
                heapq.heappush(heap,count)
            
            if heap:
                #if we have valid elements to process, remove it from heap and decrement
                count=heapq.heappop(heap)
                count+=1    #decrement max heap

                if count<0:
                     #valid elems still exist 
                    cooldown.append((time+n+1,count))
        return time




        