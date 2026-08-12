class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        l = len(nums)
        c=0
        zero=0
        maxi=0
        for right in range(l):
            if nums[right]==1:
                c+=1
            else:
                zero+=1
            while zero>k:
                if nums[left]==1:
                    c-=1
                else:
                    zero-=1
                left+=1
            maxi = max(maxi,c+zero)
        return maxi                