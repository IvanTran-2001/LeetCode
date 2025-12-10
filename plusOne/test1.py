class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)
        digits[length - 1] += 1
        for i in range(length):
            index = length - 1 - i
            if digits[index] < 10:
                break
            else:
                digits[index] = 0
                if i < length - 1:
                    digits[index - 1] += 1
                else:
                    digits.insert(0,1)
        
        return digits