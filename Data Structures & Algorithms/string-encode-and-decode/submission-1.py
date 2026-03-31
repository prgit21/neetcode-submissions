class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+'#'+s
        return res
            

    def decode(self, s: str) -> List[str]:
        res,i =[],0
        
        while i < len(s):
            
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i=j+1+length
        return res


#encode -> empty res and then iterate over input and add count + delimiter and then the string

#decode -> res, i is empty
            #iterate over the str and find index till delimiter, 
            #slice that part of string and add it to res
            #update the i pointer by setting the j +length +1