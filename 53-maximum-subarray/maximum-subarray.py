class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sums = 0
        for num in nums:
            sums += num
            maxi = max(maxi,sums)
            if sums<0:
                sums = 0
        return maxi