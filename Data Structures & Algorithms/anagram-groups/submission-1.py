class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            count =[0]*26
            for c in s:
                count[ord(c)-ord("a") ]+=1
            res[tuple(count)].append(s)
        return list(res.values())


        
        
        

        
        
# init default dict
# parse through list of string like for s in strs:
#init count for all 26 elem
#for c in s: -> count the occurence and update in count str
# return list of all elements as sublists with same count