class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        if l1>l2:
            l = l1-l2
            b = "0"*l+b
        elif l1<l2:
            l = l2-l1
            a = "0"*l+a
        l = len(a)
        carry = 0
        res = ""
        print(a,b)
        for i in range(l-1,-1,-1):
            sums = carry+int(a[i])+int(b[i])
            if sums==3:
                res = "1"+res
                carry = 1
            elif sums==2:
                res = "0"+res
                carry = 1
            elif sums==1:
                res = "1"+res
                carry = 0
            elif sums==0:
                res = "0"+res
                carry = 0
        if carry>0:
            res = str(carry)+res
        return res