class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brut force -> count existence of every element, return 2 top freq
        #store highest frequence array, reverse it and return k elem
        
        freq={} #to build frequency map of number of times n item is seen

        for num in nums: #build out the frequency map now
            freq[num]= 1+ freq.get(num,0)

        #need to sort the freq in desc 

        res=sorted(freq.items(),key= lambda x:x[1], reverse=True)

        res=res[:k]
        ans=[]

        for x in res:
            ans.append(x[0])
        return ans