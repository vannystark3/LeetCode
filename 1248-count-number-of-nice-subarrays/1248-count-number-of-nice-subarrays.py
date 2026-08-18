class Solution:
    def atMost(self,nums,k):
        l = len(nums)
        odd = 0
        left=0
        res=0
        for right in range(l):
            if nums[right]%2!=0:
                odd+=1
            while odd>k:
                if nums[left]%2!=0:
                    odd-=1
                left+=1
            res+=(right-left+1)
        return res
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k)-self.atMost(nums,k-1)