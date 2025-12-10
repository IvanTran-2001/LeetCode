class Solution(object):
    def subarraysDivByK(self, nums, k):
        
        my_dict = {0:0}
        
        sum = 0
        count = 0
        
        for i in nums:
            
            sum += i
            sum = sum%k
            
            if sum in my_dict:
                my_dict[sum] += 1
                count += my_dict[sum]
            else:
                my_dict[sum] = 0
            
            

        return count

if __name__ == "__main__":
    yes = Solution()

    print(yes.subarraysDivByK([4,5,0,-2,-3,1,7,5,2,3,0,0], 5))

