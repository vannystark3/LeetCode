class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        l = len(nums)
        left=0
        sums=0
        for right in range(l):
            sums+=nums[right]
            while sums>=target:
                mini = min(mini,right-left+1)
                sums-=nums[left]
                left+=1
        return 0 if mini==float('inf') else mini