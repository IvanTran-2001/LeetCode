from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k*m > len(bloomDay):
            return -1

        unique_numbers = sorted(set(bloomDay))
        for lowest in unique_numbers:
            before = 1
            m_count = 0
            k_count = 0
            for i in range(len(bloomDay)): 

                if before != 0:
                    k_count = 0
                    
                if bloomDay[i] - lowest <= 0:
                    k_count += 1
                    before = 0
                else:
                    before = 1
                    
                if k_count == k:
                    m_count += 1
                    if m_count == m:
                        return lowest
                    k_count = 0
                    
        
        return -1

if __name__ == "__main__":
    yes = Solution()

    print(yes.minDays([1,10,3,10,2], 3, 1))

