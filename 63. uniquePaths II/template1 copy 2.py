from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m=len(obs)
        n=len(obs[0])
        dp=[0]*(n)
        dp[0]=1
        for i in range(m):
            for j in range(n):
                if obs[i][j]==0:
                    if j:
                        dp[j]+=dp[j-1]
                else:
                    dp[j]=0
        return dp[-1]

if __name__ == "__main__":
    yes = Solution()
    matrix = [[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,1,0,0],[0,0,0,0]]

    
    print(yes.uniquePathsWithObstacles(matrix))