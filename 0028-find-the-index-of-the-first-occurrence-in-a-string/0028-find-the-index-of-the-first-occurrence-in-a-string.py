class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        m = len(needle)
        for i in range(l-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1