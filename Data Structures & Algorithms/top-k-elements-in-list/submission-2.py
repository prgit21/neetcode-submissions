class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brut force -> count existence of every element, return 2 top freq
        #store highest frequence array, reverse it and return k elem
        freq={}
        #build highest frequency array
        
        for num in nums:
            freq[num]=1 + freq.get(num,0)  #builds freq map with num as key
        #srot the freq map to ensure we sort on 2nd elem(the value and do it in desc)

        res=sorted(freq.items(),key=lambda x:-x[1])

        #return top k elem from list of tuples

        #slice res to get first k elem

        res=res[:k]
        ans=[]
        for x in res:
            ans.append(x[0])
        return ans

