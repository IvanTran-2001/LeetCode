class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = {'(':0, '[':0 , '{':0}
        close = {')':'(', ']':'[' , '}':'{'}

        stack = []
        length = len(stack) 

        if length%2 != 0:
            return False
        
        try:
            for i in s:
                if i in open:
                    stack.append(i)
                else:
                    if stack.pop() != close[i]:
                        return False
                    
        except Exception:
            return False
        
        if len(stack) != 0:
            return False
        
        return True


if __name__ == "__main__":
    s = "{[]}"

    yes = Solution()

    print(yes.isValid(s))