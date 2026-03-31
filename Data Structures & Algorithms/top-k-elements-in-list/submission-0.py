class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}     
        frequency=[[]for i in range(len(nums)+1)]   

        for n in nums:
            count[n]=1+count.get(n,0)

        for n,c in count.items():
            frequency[c].append(n)
            
        res=[]
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res)==k:

                    return res


        #init dict to count number of times an element is repeated
        #init freq count list of list and +1 to cover even spread edge case
        #build freq list by looping thgough count.items and appending to freq
        # traverse array in reverse and append to res k times


                                        