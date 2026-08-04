class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = len(num)
        for i in range(l-1,-1,-1):
            n = int(num[i])
            if n%2!=0:
                return num[:i+1]
        return ""