from collections import deque
class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        new_array = list(s)
        start = 0
        pop_list = deque()
        
        while start < len(new_array):
            if new_array[start].isdigit():
                new_array[start] = ""
                if pop_list:
                    new_array[pop_list.pop()] = ""
            else:
                pop_list.append(start)
            
            start += 1
            
        return "".join(new_array)

if __name__ == "__main__":
    yes = Solution()

    print(yes.clearDigits("ag3"))

