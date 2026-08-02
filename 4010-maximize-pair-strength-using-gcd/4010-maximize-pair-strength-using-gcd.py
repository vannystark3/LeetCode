class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = 0
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                ans = (nums[i]*nums[j])//(math.gcd(nums[i],nums[j]))**2
                maxi = max(ans,maxi)
        return maxi