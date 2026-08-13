class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l = len(s)
        left = 0
        d = set()
        for right in range(l):
            while s[right] in d:
                d.remove(s[left])
                left+=1
            d.add(s[right])
            maxi = max(maxi,right-left+1)
        return maxi