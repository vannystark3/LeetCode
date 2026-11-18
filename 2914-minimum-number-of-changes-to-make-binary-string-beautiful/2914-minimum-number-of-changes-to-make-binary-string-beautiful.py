class Solution:
    def minChanges(self, s: str) -> int:
        c = 0
        l = len(s)
        for i in range(0,l,2):
            if s[i]!=s[i+1]:
                c+=1
        return c