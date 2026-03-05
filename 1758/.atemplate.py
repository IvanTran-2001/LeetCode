from typing import List

class Solution:
    def minOperations(self, s: str):
        n = len(s)
        num = int(s, 2)  # Convert binary string to integer
        
        # Generate 1010... and 0101... masks of length n
        mask_a = int("10" * (n // 2) + ("1" if n % 2 else ""), 2)  # 101010...
        mask_b = int("01" * (n // 2) + ("0" if n % 2 else ""), 2)  # 010101...
        
        # XOR gives differing bits, popcount gives number of mismatches
        count_a = bin(num ^ mask_a).count("1")
        count_b = bin(num ^ mask_b).count("1")
        
        return min(count_a, count_b)

if __name__ == "__main__":
    yes = Solution()

    print(yes.minOperations("0100"))

