class Solution:
    def checkPallindrom(self,s,low,high,l):
        while low>=0 and high<l and s[low]==s[high]:
            low-=1
            high+=1
        return s[low+1:high]
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        maxi = s[0]
        if l==1:
            return s
        for i in range(l-1):
            odd = self.checkPallindrom(s,i,i,l)
            even = self.checkPallindrom(s,i,i+1,l)
            if len(odd)>len(maxi):
                maxi = odd
            if len(even)>len(maxi):
                maxi = even
        return maxi

