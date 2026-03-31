class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force -> init profit to 0, and then compute value from every single index repetirively to find max val
        #optimsied -> use sliding window, init both l and r to ensure window expands, when profit 

        l,r=0,1
        maxp=0

        while r < len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(profit,maxp)
                r+=1
            else:
                l=r
                r+=1
        return maxp