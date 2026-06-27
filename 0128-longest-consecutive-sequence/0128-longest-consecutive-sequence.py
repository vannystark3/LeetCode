class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        maxii = 0
        for num in a:
            if num-1 not in a:
                curr = 1
                while num+1 in a:
                    curr += 1
                    num += 1
                maxii = max(maxii,curr)
        return maxii