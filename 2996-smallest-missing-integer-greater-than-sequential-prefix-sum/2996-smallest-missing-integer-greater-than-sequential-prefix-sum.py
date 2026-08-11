class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = len(nums)
        d = set(nums)
        pre = nums[0]
        for i in range(1,l):
            if nums[i]!=(nums[i-1]+1):
                break
            pre += nums[i]
        while pre in d:
            pre+=1
        return pre         