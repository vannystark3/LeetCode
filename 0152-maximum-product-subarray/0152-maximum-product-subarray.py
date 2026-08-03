class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        maxi=float('-inf')
        l = len(nums)
        for i in range(l):
            if nums[i]==0:
                maxi = max(0,maxi)
                prefix=1
                continue
            prefix*=nums[i]
            maxi=max(prefix,maxi)
        for i in range(l-1,-1,-1):
            if nums[i]==0:
                suffix=1
                continue
            suffix*=nums[i]
            maxi=max(suffix,maxi)
        return maxi