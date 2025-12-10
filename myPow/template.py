class Solution(object):

    def myPow(self, x, n):
        
        if n == 1:
            return x
        elif n == -1:
            return (1/x)
        elif n < 0:
            return (1/x) * self.myPow(x, n + 1)
        elif n > 0:
            return  x * self.myPow(x, n - 1)
        else:
            return 1
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.myPow(2, -4))