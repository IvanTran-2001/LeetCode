class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = -1
        length = len(s)
        count = 0
        while index >= -(length):
            if (s[index] >= 'a' and s[index] <= 'z') or (s[index] >= 'A' and s[index] <= 'Z'):
                while index >= -(length):
                    if s[index] == " ":
                        return count
                    count += 1
                    index -=1
            index -= 1
        return count
        
if __name__ == "__main__":
    yes = Solution()
    print(yes.lengthOfLastWord("a"))