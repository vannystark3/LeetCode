class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0] = 1
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = up+left
        return dp[m-1][n-1]        
