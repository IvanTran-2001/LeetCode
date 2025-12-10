class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listofZero = []
        index = 0
        length = 1

        for i in nums:
            if i == 0:
                listofZero.append(index)
                length += 1
            index += 1

        listofZero.append(index)

        maxSub = 0

        if length > 1:

            temp = listofZero[0] + (listofZero[1] - (listofZero[0]+1))
            if temp > maxSub:
                    maxSub = temp

            for i in range(length):
                if i + 2 < length:
                    temp = listofZero[i+1] - (listofZero[i]+1) + (listofZero[i+2] - (listofZero[i+1]+1))
                else:
                    break
                if temp > maxSub:
                    maxSub = temp

        else:
            return index-1

        return maxSub

            
if __name__ == "__main__":
    yes = Solution()

    print(yes.longestSubarray([1,1,0,1]))