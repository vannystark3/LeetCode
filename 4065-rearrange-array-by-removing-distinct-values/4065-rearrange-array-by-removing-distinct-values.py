class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        d = {}
        ans = []
        for num in nums:
            d[num] = d.get(num,0)+1
        l = max(d.values())
        i = 0
        while l>i:
            for k in d:
                if d[k]==0:
                    continue
                ans.append(k)
                d[k] -= 1
            i+=1
        return ans