class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        fPrice = prices[0]
        sPrice = prices[0]
        maxProfit = 0
        
        for c in prices:
            
            if (c - fPrice) > maxProfit:
                maxProfit = c - fPrice
                
            if sPrice > c:
                sPrice = c
                
            if (c - sPrice) > maxProfit:
                fPrice = sPrice
                maxProfit = c - fPrice
            
                
        return maxProfit
                
                
            
            
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.maxProfit([7,1,5,3,6,4]))