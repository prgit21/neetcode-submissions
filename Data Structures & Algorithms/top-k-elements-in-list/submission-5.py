class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brut force -> count existence of every element, return 2 top freq
        
        #need to create a frequency map of all elements that occur

        #sort the frequency map by descending and then accum top k elem

       #create a frequency bucket so we can store the count of each item

       freq= [ [] for _ in range(len (nums)+1)]

       count={}

       for num in nums:
            count[num]=1+count.get(num,0)

       for number,cnt in count.items():
        freq[cnt].append(number)

       ans=[]
       for x in range((len(freq)-1),0,-1):
        for ns in freq[x]:
            ans.append(ns)

            if len(ans)==k:
                return ans



        