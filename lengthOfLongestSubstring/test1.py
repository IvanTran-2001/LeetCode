class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        front = 0
        back = 0
        length = len(s)
        found = {}
        maxL = 0

        while back < length:
            if s[back] not in found:
                found[s[back]] = ''
            else:
                if length - front < maxL:
                    break
                maxL = max(maxL, back - front)
                
                while s[back] != s[front]:
                    del found[s[front]]
                    front += 1
                front += 1

            back += 1

        return max(maxL, back - front)
        
if __name__ == "__main__":
    yes = Solution()
    print(yes.lengthOfLongestSubstring("cdd"))