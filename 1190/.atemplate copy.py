from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pop_list = deque()
        i = 0

        while i < len(s):
            if s[i] == '(':
                pop_list.append(i)
            elif s[i] == ')':
                j = pop_list.pop()
                s = s[0:j] + s[j+1:i][::-1] + s[i+1:]
                i -= 2
            
            i += 1
        
        return s

if __name__ == "__main__":
    yes = Solution()
    print(yes.reverseParentheses("(u(love)i)"))
