from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        start = 0
        word = ""
        i = 0
        cords = None

        while i < len(s):
            if s[i] == "(":
                word += s[start:i]
                cords = reverse(i, s)
                word = word + cords[0]
                i = cords[1]
                start = i 
            else:
                i += 1
        
        if word == "":
            return s
        
        if cords and cords[1] < len(s):
            return word + s[cords[1]:]
        
        return word


def reverse(index, s):
    r = index
    pop_list = deque()
    word = ""
    count = 0

    while r < len(s):
        if s[r] == ')':
            count -= 1
            if count == 0:
                break
            else:
                count += 1
        elif s[r] == '(':
            count += 1
            pop_list.append(r)
        
        r += 1
        
    before_left = ""
    before_right = ""
    if pop_list:
        before_left = pop_list.pop()
        before_right = r
        word = s[before_left + 1: r]
        word = word[::-1]

    r += 1
    if len(s) <= r:
        return [word, r]
    while pop_list:
        if s[r] == ")":
            temp = pop_list.pop()
            word = s[temp + 1: before_left] + word + s[before_right + 1: r]
            word = word[::-1]
            before_left = temp
            before_right = r

        r += 1
        
    return [word, r]

if __name__ == "__main__":
    yes = Solution()
    print(yes.reverseParentheses("n(ev(t)((()lfevf))yd)cb()"))
