class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        mini = nums[0]
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<mini:
                mini = nums[mid]
            if nums[mid]>nums[r] and nums[r]<nums[l]:
                l = mid+1
            else:
                r = mid-1
        return mini