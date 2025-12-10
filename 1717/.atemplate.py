from typing import List
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        count_a = 0
        count_b = 0
        total = 0
        sum = 0
        letter_a = 'a'
        letter_b = 'b'
        i, j = -1, -1
        if x > y:
            x, y = y, x
            letter_a, letter_b = letter_b, letter_a

        for c in s:
            j += 1
            stringt = s[i + 1:j + 1]
            if c == letter_a:
                count_a += 1
                if count_b > 0:
                    sum += y
                    count_b -= 1
                    count_a -= 1
                elif total > 0:
                    total += -x
                    sum += y
                
            elif c == letter_b:
                count_b += 1
                if count_a > 0:
                    total += x
                    count_a -= 1
                    count_b -= 1
            else:
                i = j
                sum += total
                total = 0
                count_a = 0
                count_b = 0
            
                
        sum += total
        return sum

if __name__ == "__main__":
    yes = Solution()

    print(yes.maximumGain("bbabbabba", 8484, 4096))

