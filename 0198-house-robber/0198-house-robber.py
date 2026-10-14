class Solution:
    def f(self,dp,nums,a):
        if a==0:
            return nums[0]
        if a<0:
            return 0
        if dp[a]!=-1:
            return dp[a]
        pick = nums[a]+self.f(dp,nums,a-2)
        notpick = self.f(dp,nums,a-1)
        dp[a] = max(pick,notpick)
        return dp[a]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        dp[0] = 0
        return self.f(dp,nums,n-1)