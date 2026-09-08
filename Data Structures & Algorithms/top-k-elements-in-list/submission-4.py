class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brut force -> count existence of every element, return 2 top freq
        
        #need to create a frequency map of all elements that occur

        #sort the frequency map by descending and then accum top k elem

       #create a frequency bucket so we can store the count of each item

       freq=[ [] for _ in range(len(nums)+1)] 
       count={} 
       #map to store key,value of frequency
       for num in nums:
        count[num]=1+count.get(num,0)
       
       #now we have to fill in freq count into freq map

       for number,cnt in count.items():
        freq[cnt].append(number)
       #this appends count of number of times an element is seen to its value
       #i.e we see all elements repeated 3 times have value 5

       res=[]

       for x in range((len(freq)-1),0,-1):
        for res_val in freq[x]:
            res.append(res_val)
        
            if len(res)==k:
                return res

        

    

    

       