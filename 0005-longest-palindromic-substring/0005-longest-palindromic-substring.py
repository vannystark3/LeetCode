class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
        c = 1
        ans = s[0]
        for i in range(l):
            st = s[i]
            for j in range(i+1,l):
                st += s[j]
                if st==st[::-1] and len(st)>c:
                    c = len(st)
                    ans = st
        return ans                        