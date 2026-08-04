class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        c=0
        for ch in s:
            if ch=='(':
                c+=1
                maxi=max(maxi,c)
            elif ch==')':
                c-=1
        return maxi