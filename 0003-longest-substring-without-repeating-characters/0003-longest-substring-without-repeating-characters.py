class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l = len(s)
        left = 0
        d = {}
        for right in range(l):
            if s[right] not in d or d[s[right]]<left:
                d[s[right]] = right
            else:
                left = d[s[right]]+1
                d[s[right]] = right
            maxi = max(maxi,right-left+1)
        return maxi