class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a,b,c = -1,-1,-1
        l = len(s)
        res = 0
        for right in range(l):
            if s[right]=='a':
                a = right
            elif s[right]=='b':
                b = right
            else:
                c = right
            if a!=-1 and b!=-1 and c!=-1:
                res += (min(a,b,c)+1)
        return res
            
