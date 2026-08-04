class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        arr = []
        for k in d:
            arr.append((d[k],k))
        arr.sort(reverse=True)
        s = ""
        for freq,k in arr:
            s += (k*freq)
        return s