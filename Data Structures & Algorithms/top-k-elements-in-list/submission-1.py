class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency =[[] for _ in range(len(nums)+1)] # create a frequency bucket

        for n in nums:  #go thru list and populate frequency bucket
            count[n]=1+ count.get(n,0)          
            #assign a default of 0, otherwise count of element n at position n
        
        for n,c in count.items():
            frequency[c].append(n)      
            #append the frequency bucket index at each pos to its value
        res=[]

        for i in range(len(frequency)-1,0,-1):      #reverse string
            for n in frequency[i]:     #loop to append to res
                res.append(n)
                if len(res)==k:
                    return res

