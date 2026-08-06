class Solution:
    def beautySum(self, s: str) -> int:
        l = len(s)
        res = 0
        for i in range(l):
            d = {}
            for j in range(i,l):
                if s[j] not in d:
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1
                v = d.values()
                res += (max(v)-min(v))
        return res
