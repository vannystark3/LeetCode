class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for s in word:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        arr = list(d.values())
        arr.sort(reverse=True)
        l = len(arr)
        res = 0
        for i in range(l):
            k = i//8
            k+=1
            res+=(arr[i]*k)
        return res