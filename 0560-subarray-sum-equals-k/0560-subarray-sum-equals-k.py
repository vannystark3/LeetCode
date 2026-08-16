class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        d = {0:1}
        c = 0
        for num in nums:
            pre += num
            if pre-k in d:
                c += d[pre-k]
            if pre in d:
                d[pre] += 1
            else:
                d[pre] = 1
        return c