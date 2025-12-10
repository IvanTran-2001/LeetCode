from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        my_dict = {}
        possible = False
        for i in flights:
            my_dict[i[0]] = my_dict.get(i[0], {})
            my_dict[i[0]][i[1]] = my_dict[i[0]].get(i[1], deque())
            my_dict[i[0]][i[1]].append(i[2])
            if i[1] == dst:
                 possible = True
        
        if not possible:
            return -1
        
        

if __name__ == "__main__":
    yes = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1

    print(yes.findCheapestPrice(n, flights, src, dst, k))

