import math
class Solution(object):
    def __init__(self):
        self.answer = ""
        self.new_array = []
    def getPermutation(self, n, k):
        for i in range(n):
            self.new_array.append(chr(49 + i))
            
        return self.recurse(n, k)
    
    def recurse(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return self.answer
        else:
            index = 0
            factorial_limit = math.factorial(n - 1)
            while k - factorial_limit > 0:
                index += 1
                k -= factorial_limit
            
            self.answer = self.answer + self.new_array[index]
            del self.new_array[index]
            
            
            return self.recurse(n - 1, k)
            
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.getPermutation(3, 6))