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
            m = max(d.values())
            while sums-m>k:
                if d[s[left]]>1:
                    d[s[left]] -= 1
                else:
                    del d[s[left]]
                left += 1
                sums -= 1
                m = max(d.values())        
            maxi = max(maxi,right-left+1)
        return maxi