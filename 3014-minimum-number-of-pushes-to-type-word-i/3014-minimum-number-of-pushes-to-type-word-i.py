class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        i = 1
        res = 0
        while l!=0:
            if l>=8:
                res += (i*8)
                l -= 8
            else:
                res += (i*l)
                l -= l
            i += 1
        return res