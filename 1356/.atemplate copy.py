class Solution:
    def sortByBits(self, arr):
        bit_table = [bin(i).count('1') for i in range(10001)]  # precompute
        return sorted(arr, key=lambda x: (bit_table[x], x))
    
    
if __name__ == "__main__":
    yes = Solution()
    print(yes.sortByBits([0,1,2,3,4,5,6,7,8]))

