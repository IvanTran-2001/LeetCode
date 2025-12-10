class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min = prices[0]
        max = 0
        maxProfit = 0
        
        for c in prices:
            
            if c < min:
                min = c
                max = 0
                
            if c > max:
                max = c
                profit = max - min
                if profit > maxProfit:
                    maxProfit = profit
            
                
        return maxProfit
        
if __name__ == "__main__":
    test = Solution()
    print(test.maxProfit([7,1,5,3,6,4]))