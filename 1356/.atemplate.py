class Solution:
    def sortByBits(self, arr):
        binary = map(lambda x: bin(x).count('1'), arr)

        result = [v for _, v in sorted(zip(binary, arr))]

        return result
if __name__ == "__main__":
    yes = Solution()
    print(yes.sortByBits([0,1,2,3,4,5,6,7,8]))

