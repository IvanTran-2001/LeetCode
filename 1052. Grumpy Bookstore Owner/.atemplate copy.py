from typing import List
from collections import deque

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        value = 0
        Ones_List = []
        for i in range(len(customers)):
            if grumpy[i] == 0:
                value += customers[i]
            else:
                Ones_List.append(i)
        
        maximum_val = value
        if minutes > 0 and Ones_List:
            start = 0
            index_count = 1
            value += customers[Ones_List[0]]
            maximum_val = value
            for i in range(1, len(Ones_List)):
                value += customers[Ones_List[i]]
                index_count += Ones_List[i] - Ones_List[i - 1]
                while start < len(Ones_List) and index_count > minutes:
                    value -= customers[Ones_List[start]]
                    index_count -= Ones_List[start + 1] - Ones_List[start]
                    start += 1
                    
                maximum_val = max(maximum_val, value)
        
        return maximum_val
            

if __name__ == "__main__":
    yes = Solution()
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3

    print(yes.maxSatisfied(customers, grumpy, minutes))

