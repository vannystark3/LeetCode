class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = len(nums)
        if l==1:
            return True
        inc=True
        dec=True
        for i in range(l-1):
            if nums[i]<nums[i+1]:
                dec=False
            elif nums[i]>nums[i+1]:
                inc=False
        return inc or dec