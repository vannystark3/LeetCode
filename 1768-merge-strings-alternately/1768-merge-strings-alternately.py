class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1 = len(word1)
        l2 = len(word2)
        l = l1 if l1<l2 else l2
        for i in range(l):
            res += f"{word1[i]}{word2[i]}"
        if l1>l2:
            res += word1[l:]
        if l2>l1:
            res += word2[l:]
        return res 