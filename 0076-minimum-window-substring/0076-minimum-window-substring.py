class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        dt = {}
        for ch in t:
            if ch not in dt:
                dt[ch] = 1
            else:
                dt[ch] += 1
        have,need = 0,len(dt)
        left = 0
        l = len(s)
        ds = {}
        res = ""
        mini = float('inf')
        for right in range(l):
            el = s[right]
            if el not in ds:
                ds[el] = 1
            else:
                ds[el] += 1
            if el in dt and ds[el]==dt[el]:
                have += 1
            while have==need:
                if mini>right-left+1:
                    mini = right-left+1
                    res = s[left:right+1]
                ds[s[left]] -= 1
                if s[left] in dt and ds[s[left]]<dt[s[left]]:
                    have-=1
                left+=1
        return res