class Solution:
    def countAtMost(self,nums,k):
        if k<0:
            return 0
        l = len(nums)
        left=0
        sums=0
        res = 0
        for right in range(l):
            sums+=nums[right]
            while sums>k and left<l:
                sums-=nums[left]
                left+=1
            res+=(right-left+1)
        return res
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.countAtMost(nums,goal)-self.countAtMost(nums,goal-1)