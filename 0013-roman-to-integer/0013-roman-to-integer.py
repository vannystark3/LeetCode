class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l = len(s)
        res = 0
        for i in range(l-1,-1,-1):
            if i<l-1 and d[s[i]]<d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res