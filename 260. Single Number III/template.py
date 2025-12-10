class Solution(object):
    def singleNumber(self, nums):
        # Step 1: XOR all elements in the array
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Find the rightmost set bit in xor_result
        rightmost_set_bit = xor_result & -xor_result
        
        # Step 3: Partition the array based on the rightmost set bit
        a = 0
        b = 0
        for num in nums:
            if num & rightmost_set_bit:
                # XOR elements in the first subarray
                a ^= num
            else:
                # XOR elements in the second subarray
                b ^= num
        
        return a, b
        
        
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.singleNumber([1,2,1,3,2,5]))

