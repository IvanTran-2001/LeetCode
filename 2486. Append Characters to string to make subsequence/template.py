class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t_index = 0
        for i in s:
            if i == t[t_index]:
                t_index += 1
                if t_index == len(t):
                    return 0
        
        return len(t) - t_index
        
if __name__ == "__main__":
    yes = Solution()
    s,t = "b", "abcde"

    print(yes.appendCharacters(s, t))

