from typing import List
import heapq

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        min_difficulty = [(d, p) for d, p in (zip(difficulty, profit))]
        heapq.heapify(min_difficulty)
        heapq.heapify(worker)
        max_value = [0,0]
        profit = 0
        while worker:
            dif = heapq.heappop(worker)
            
            while min_difficulty and min_difficulty[0][0] <= dif:
                temp = heapq.heappop(min_difficulty)
                
                if temp[0] <= dif:
                    if max_value[0] <= temp[1]:
                        max_value[0] = temp[1]
                        max_value[1] = temp[0]
            
            if max_value[1] <= dif:
                profit += max_value[0]
        
        return profit
            
        

if __name__ == "__main__":
    yes = Solution()
    difficulty = [0]
    profit = [-1]
    worker = [0]

    print(yes.maxProfitAssignment(difficulty, profit, worker))

