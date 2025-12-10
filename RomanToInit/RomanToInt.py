class Solution(object):

    def romanToInt(self, s):

        romanLetters = ["I", "V", "X", "L", "C", "D", "M"]
        romanToNum = [1, 5, 10, 50, 100, 500, 1000]
        max = 6
        sum = 0

        for letter in s:

            while (True):

                if (max < 0):
                    break

                elif letter == romanLetters[max]:
                    sum += romanToNum[max]
                    break

                else:

                    if (5 > max):

                        if (letter == romanLetters[max + 2]):
                            sum -= romanToNum[max]*2
                            sum +=  romanToNum[max + 2]
                            break

                        elif ((letter == romanLetters[max + 1])):
                            sum -= romanToNum[max]*2
                            sum +=  romanToNum[max + 1]
                            break
                    
                    max -= 1
        
        return sum

if __name__ == "__main__":
    roman = Solution()
    print(roman.romanToInt("MCDLXXVI"))