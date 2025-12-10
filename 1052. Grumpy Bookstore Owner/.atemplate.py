
from typing import List
from collections import deque

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        counter = 0
        value = 0
        maximum_val = 0
        pop_list = deque()
        for i in range(len(customers)):
            if grumpy[i] == 0:
                value += customers[i]
        i = 0    
        while i < len(grumpy):
            if grumpy[i] == 1 and minutes > 0:
                
                if counter >= minutes:
                    
                    while pop_list and i - pop_list[0][0] >= minutes:
                        value -= pop_list[0][1]
                        counter += pop_list.popleft()[0] 
                        if pop_list:
                            counter -= pop_list[0][0]
                    
                    if not pop_list:
                        counter = 0
                
                value += customers[i]
                pop_list.append([i, customers[i]])
                
            
            maximum_val = max(maximum_val, value)

            counter += 1
            i += 1
        
        return maximum_val

if __name__ == "__main__":
    yes = Solution()
    customers = [2,4,1,4,1]
    grumpy = [1,0,1,0,1]
    minutes = 1

    print(yes.maxSatisfied(customers, grumpy, minutes))

