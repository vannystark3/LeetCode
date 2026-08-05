class Solution:
    def myAtoi(self, s: str) -> int:
        arr = list(s.strip())
        res = 0
        sign = 1 
        index = 0
        for ch in arr:
            if index==0 and ch=='-':
                sign = -1
                index = 1
            elif index==0 and ch=='+':
                index=1
                sign=1
            elif index==0 and ch==" ":
                continue
            elif index!=0 and ch==" ":
                break
            elif ch.isdigit():
                index=1
                res *= 10
                res += int(ch)
            else:
                break
            print(res)
        if sign==1:
            if res>=(2**31-1):
                return 2**31-1
            return res
        else:
            if res>=(2**31):
                return -2**31
            return -res