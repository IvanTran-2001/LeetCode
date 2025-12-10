class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        minValue = a
        maxValue = b

        if (len(a) > len(b)):
            maxValue = a
            minValue = b

        returnValue = ""
        remainder = False
        changed = False

        for i in range(1, len(maxValue) +1):

            if ((changed == False) and (len(minValue) < i)):
                changed = True
            
            if (remainder):
                if (maxValue[-i] == '0'):
                    if (changed or (minValue[-i] == '0')):
                        returnValue += "1"
                        remainder = False
                    else:
                        returnValue += "0"
                else:
                    if (changed or (minValue[-i] == '0')):
                        returnValue += "0"
                    else:
                        returnValue += "1"
            
            else:
                if (maxValue[-i] == '0'):
                    if (changed or (minValue[-i] == '0')):
                        returnValue += "0"
                    else:
                        returnValue += "1"
                    remainder = False
                else:
                    if (changed or (minValue[-i] == '0')):
                        returnValue += "1"
                    else:
                        returnValue += "0"
                        remainder = True

        if (remainder):
            returnValue += "1"             
                

        
        return returnValue[::-1]

if __name__ == "__main__":
    yes = Solution()
    print(yes.addBinary("1010", "1011"))
        
