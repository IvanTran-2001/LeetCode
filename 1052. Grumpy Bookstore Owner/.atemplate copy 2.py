from typing import List
from collections import deque

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        value = 0
        pop_list = deque()
        max_value = 0
        value_2 = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                value += customers[i]
            elif minutes > 0:
                pop_list.append(i)
                value_2 += customers[i]
                while pop_list and pop_list[-1] - pop_list[0] >= minutes:
                    value_2 -= customers[pop_list.popleft()]
                
                max_value = max(max_value, value_2)
        
        return value + max_value
        

            

if __name__ == "__main__":
    yes = Solution()
    customers = [2,6,6,9]
    grumpy = [0,0,1,1]
    minutes = 1

    print(yes.maxSatisfied(customers, grumpy, minutes))

