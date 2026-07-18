class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        c = 0
        d = {0:1}
        for num in nums:
            presum += num
            diff = presum-k
            if diff in d:
                c += d[diff]
            if presum in d:
                d[presum] += 1
            else:
                d[presum] = 1
        return c