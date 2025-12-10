from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        
        if len(s)<len(t):
            return ""
        if s == t:
            return s
        
        my_dict = {}
        order_of_t = []
        end_point = 0
        
        for c in t:
            if not(c in my_dict):
                my_dict[c] = [1,[deque(), deque()]]
            else:
                my_dict[c][0] += 1
        
        for i, c in enumerate(s):
            if c in my_dict:
                order_of_t.append(c)
                my_dict[c][1][1].append(i)
        
        for c in my_dict:
            for _ in range(my_dict[c][0]):
                if my_dict[c][1][1]:
                    popped_val = (my_dict[c][1][1].popleft())
                    if popped_val > end_point:
                        end_point = popped_val
                    my_dict[c][1][0].append(popped_val)
                else:
                    return ""
        
        minimum_coord = [my_dict[order_of_t[0]][1][0][0], end_point]
        
        for i in range(len(order_of_t) - 1):
            
            my_dict[order_of_t[i]][1][0].popleft()
            
            if my_dict[order_of_t[i]][1][1]:
                my_dict[order_of_t[i]][1][0].append(my_dict[order_of_t[i]][1][1].popleft())
                if my_dict[order_of_t[i]][1][0][-1] > end_point:
                    end_point = my_dict[order_of_t[i]][1][0][-1]
            else:
                break
            
            if minimum_coord[1] - minimum_coord[0] > end_point - my_dict[order_of_t[i + 1]][1][0][0]:
                minimum_coord[0], minimum_coord[1] = my_dict[order_of_t[i + 1]][1][0][0], end_point
            
        return s[minimum_coord[0]:minimum_coord[1] + 1]
    

if __name__ == "__main__":
    yes = Solution()
    

    print(yes.minWindow("ADOBECODEBANC", "ABC"))

