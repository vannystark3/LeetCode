class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1!=l2:
            return False
        d = {}
        for i in range(l1):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                if d[s[i]] != t[i]:
                    return False
        return True