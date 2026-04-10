class Solution:
    def minimumDistance(self, nums):
        dict_num = {}
        ans = -1

        for i, num in enumerate(nums):
            if not(num in dict_num):
                dict_num[num] = []
                dict_num[num].append(i)
            else:
                dict_num[num].append(i)
        
        for val in dict_num.values():
            if len(val) >= 3:
                i = 2
                sum = abs(val[0] - val[1]) + abs(val[1] - val[2]) + abs(val[2] - val[0])

                while i < len(val):
                    if ans == -1:
                        ans = sum
                    else:
                        sum -= abs(val[i - 3] - val[i - 2]) 
                        sum -= abs(val[i - 3] - val[i - 1]) 
                        sum += abs(val[i] - val[i - 2])
                        sum += abs(val[i - 1] - val[i-2])

                        ans = min(sum, ans)
                
                    i += 1

                        
        
        return ans

if __name__ == "__main__":
    yes = Solution()
    arr = [6,1,6,1,6,6] 

    print(yes.minimumDistance(arr))

