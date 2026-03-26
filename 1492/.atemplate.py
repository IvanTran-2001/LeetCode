class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0: return i
                if i * i != n:
                    factors.append(n // i)
        
        return factors[-k] if k <= len(factors) else -1