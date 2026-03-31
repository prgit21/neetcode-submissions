class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=collections.deque()
        l=r=0

        while r< len(nums):
            while q and nums[q[-1]]< nums[r]: #build monotonic decreasing queue
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()

            if(r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output

#init output,l and r ptr, and deque
# expand r pointer in range of nums
# while q exists and nums[q[-1]]< nums[r] -> store indice of element in descending order
#pop q and append r 

#if l > q[0] -> out of window, remove out of window elements by q.popLeft()
#when window size reaches k -> if(r+1)>=k 
#add the largest value to output (op.append(nums[q[0]]) and increment l ptr
#then increment right window
#return output