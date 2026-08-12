class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        l = len(nums)
        zero=0
        maxi=0
        for right in range(l):
            if nums[right]==0:
                zero+=1
            if zero<=k:
                maxi = max(maxi,right-left+1)
            else:
                if nums[left]==0:
                    zero-=1
                left+=1
        return maxi                