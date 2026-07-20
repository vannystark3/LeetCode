class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in h1:
                h1[ch] += 1
            else:
                h1[ch] = 1
        for ch in t:
            if ch in h2:
                h2[ch] += 1
            else:
                h2[ch] = 1
        for ch in h1:
            if ch not in h2 or h2[ch]!=h1[ch]:
                return False
        return True