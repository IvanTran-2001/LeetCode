class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x == 1):
            return 1
        min = 0
        max = x
        diff = 0

        while True:
            diff = (max + min)//2
            squar = diff*diff

            if (squar == x):
                return diff
            elif (squar > x):
                if (diff == max):
                    return diff
                max = diff
            else:
                if (diff == min):
                    return diff
                min = diff
            


        

if __name__ == "__main__":
    yes = Solution()
    print(yes.mySqrt(1))