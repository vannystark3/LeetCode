class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes==0:
                candidate = num
            if candidate==num:
                votes += 1
            else:
                votes -= 1
        return candidate