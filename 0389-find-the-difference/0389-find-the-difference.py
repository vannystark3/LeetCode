class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h1 = {}
        h2 = {}
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
        for ch in h2:
            if ch not in h1:
                return ch
            elif h2[ch]>h1[ch]:
                return ch