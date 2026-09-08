class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n))
        if l<4:
            return 0
        a = l-3
        return n-999