class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)
        dp[0] = nums[0]
        for i in range(1,n):
            if i>1:
                pick = nums[i]+dp[i-2]
            else:
                pick = nums[i]
            notpick = dp[i-1]
            dp[i] = max(pick,notpick)
        return dp[n-1]