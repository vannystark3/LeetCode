class Solution:
    def f(self,nums):
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        for i in range(n):
            take = nums[i]
            if i>1:
                take += prev2
            nottake = prev1
            curr = max(take,nottake)
            prev2 = prev1
            prev1 = curr
        return prev1

    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res1 = self.f(nums[1:])
        res2 = self.f(nums[:-1])
        return max(res1,res2)