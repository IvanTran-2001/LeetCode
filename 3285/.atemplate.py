class Solution:
    def stableMountains(self, height, threshold):
        ans = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                ans.append(i)
        
        return ans


if __name__ == "__main__":
    yes = Solution()

    print(yes.stableMountains([1,2,3,4,5], 2))
