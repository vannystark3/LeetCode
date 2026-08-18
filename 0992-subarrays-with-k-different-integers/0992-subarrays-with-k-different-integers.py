class Solution:
    def countAtMost(self,nums,k):
        left=0
        l=len(nums)
        d = {}
        res = 0
        for right in range(l):
            if nums[right] not in d:
                d[nums[right]] = 1
            else:
                d[nums[right]] += 1
            while len(d)>k:
                d[nums[left]] -= 1
                if d[nums[left]]==0:
                    del d[nums[left]]
                left+=1
            res += (right-left+1)
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.countAtMost(nums,k)-self.countAtMost(nums,k-1)