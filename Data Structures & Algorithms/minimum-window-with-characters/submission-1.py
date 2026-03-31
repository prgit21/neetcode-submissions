class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =='': return ''
        countT,window={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)

        have,need=0,len(countT)
        res,resLen=[-1,-1],float("inf")
        l=0

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c] == countT[c]:

                have+=1

            while have==need:
                if(r-l+1) < resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("infinity") else ''

#check t is empty
#init countT and window as hmap
#init countT and assign count map
#init have , need =0,len(countT)
#init res[-1,-1] and resLen(inf) and l ptr

#expand window to right -> for r in range(len(s))
#assign c=s[r] and update count of window
# increment have if the current character is one we need (exists in t)and exact count

#while have == need ( satisfied ) shrink left window to find optimum
#if window size < resLen update res and reslen
#remove character from window(check condn) and decrement lptr

#update l,r =resand return splice string from s[l:r+1]

