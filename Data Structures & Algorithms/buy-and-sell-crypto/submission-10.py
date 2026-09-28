class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force -> search for every valid combination by pinning at one index and compiting all values 
        #optimal
        #start with l0 and r one ahead
        #use r to scan ahead, if lower value of p[l] vs p[r] is found skip l ahead to that day bcs this is newest low buy day
        #update r at every iteration 

        l=0
        r=1
        maxp=0

        while r < (len(prices)):
            profit=prices[r]-prices[l]
            maxp=max(profit,maxp)

            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                r+=1
        return maxp



        