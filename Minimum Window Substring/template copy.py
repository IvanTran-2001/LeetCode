from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        my_dict = {}
        new_array = []
        n_a_index = 0
        minimum_coord = []
        for c in t:
            if not(c in my_dict):
                my_dict[c] = ([n_a_index],[deque()])
                new_array.append(my_dict[c][1][-1])
                n_a_index += 1
            else:
                my_dict[c][0].append(n_a_index)
                my_dict[c][1].append(deque())
                new_array.append(my_dict[c][1][-1])
                n_a_index += 1
        
        for i, c in enumerate(s):
            if c in my_dict:
                for t in (my_dict[c][0]):
                    beforePosition = t - 1
                    if beforePosition >= 0:
                        if new_array[beforePosition]:
                            if new_array[beforePosition][0] < i:
                                new_array[t].append(i)
                    else:
                        new_array[t].append(i)
        
        if not new_array[-1]:
            return ""
        
        minimum_coord = [new_array[0][0], new_array[-1][0] + 1]
        
        while True:
            
            new_array[0].popleft()
            
            if not new_array[0]:
                return s[minimum_coord[0]: minimum_coord[1]]
            
            for i in range(1, len(new_array)):
                while True:
                    if new_array[i][0] <= new_array[i - 1][0]:
                        new_array[i].popleft()
                    else:
                        break
                    
                    if not new_array[i]:
                        return s[minimum_coord[0]: minimum_coord[1]]
            
            if new_array[-1][0] - new_array[0][0] + 1 < minimum_coord[1] - minimum_coord[0]:
                minimum_coord = [new_array[0][0], new_array[-1][0] + 1]

                    
        
        
        
        
        
        
        

if __name__ == "__main__":
    yes = Solution()
    

    print(yes.minWindow("ccwaeabwefgewcwaefgcf", "cae"))

