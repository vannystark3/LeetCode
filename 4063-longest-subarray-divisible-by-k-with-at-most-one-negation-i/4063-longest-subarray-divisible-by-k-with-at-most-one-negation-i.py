class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        l = len(nums)
        maxi = 0
        for left in range(l):
            d = set()
            d.add(0)
            sums = 0
            for right in range(left,l):
                sums+=nums[right]
                b = (2*nums[right])%k
                d.add(b)
                a = sums%k
                if a in d:
                    maxi = max(maxi,right-left+1)
        return maxi