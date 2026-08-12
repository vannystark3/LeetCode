class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l = len(s)
        left = 0
        d = {}
        for right in range(l):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            while max(d.values())>1:
                d[s[left]]-=1
                left+=1
            maxi = max(maxi,right-left+1)
        return maxi