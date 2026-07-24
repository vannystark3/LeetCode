class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        j = 0
        for i in range(l):
            if j==0 or j==1 or nums[j-2]!=nums[i]:
                nums[j] = nums[i]
                j += 1
        return j