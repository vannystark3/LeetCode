class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0]*l
        p = 0
        n = 1
        for num in nums:
            if num>0:
                res[p] = num
                p += 2
            else:
                res[n] = num
                n += 2
        return res