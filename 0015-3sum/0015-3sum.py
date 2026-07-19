class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = l-1
            while j<k:
                sums = nums[i]+nums[j]+nums[k]
                if sums==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j]==nums[j-1] and j<k:
                        j += 1
                elif sums>0:
                    k -= 1
                else:
                    j += 1
        return res
