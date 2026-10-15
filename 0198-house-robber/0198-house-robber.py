class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        for i in range(1,n):
            take = nums[i]
            if i>1:
                take += prev2
            nottake = prev1
            curr = max(take,nottake)
            prev2 = prev1
            prev1 = curr
        return prev1