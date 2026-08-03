class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        pre = SortedList([0])
        c = 0
        sums = 0
        for num in nums:
            if num%2==0:
                sums += b
            else:
                sums -= a
            c += (len(pre)-pre.bisect_left(sums))
            pre.add(sums)
        return c