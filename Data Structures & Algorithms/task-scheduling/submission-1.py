class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n==0:
            return len(tasks)
        time=0
        freq=Counter(tasks)
        
        heap=[ -count for count in freq.values()]
        heapq.heapify(heap)
        cooldown=deque()

        while heap or cooldown:            
            time+=1

            while cooldown and cooldown[0][0]<=time:
                pass
                # when cooldown queue has values which are ready to be processed
                #pop them from the queue and add them to heap
                _,count=cooldown.popleft()
                heapq.heappush(heap,count)
                
            if heap:
                count=heapq.heappop(heap)
                count+=1

                if count <0:
                    #elements still to be processed append to cooldown 
                    cooldown.append((time+n+1,count))

        return time


