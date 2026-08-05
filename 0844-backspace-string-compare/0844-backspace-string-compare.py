class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1 = ''
        for ch in s:
            if ch=='#':
                res1 = res1[:-1]
            else:
                res1 += ch
        res2 = ''
        for ch in t:
            if ch=='#':
                res2 = res2[:-1]
            else:
                res2 += ch
        return res1==res2