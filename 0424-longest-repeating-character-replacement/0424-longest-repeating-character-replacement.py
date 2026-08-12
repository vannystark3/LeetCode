class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        l = len(s)
        maxi = 0
        d = {}
        sums = 0
        for right in range(l):
            if s[right] in d:
                d[s[right]] += 1
            else:
                d[s[right]] = 1
            sums += 1
            if sums-max(d.values())>k:
                d[s[left]] -= 1
                left += 1
                sums -= 1
            maxi = max(maxi,right-left+1)
        return maxi