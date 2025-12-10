from itertools import combinations 

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combinations([i for i in range(1,n+1)], k)
                        
                        
        
                
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.combine(4, 2))

