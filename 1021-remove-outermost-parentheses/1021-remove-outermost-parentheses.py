class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        arr = list(s)
        openn=0
        l=len(arr)
        for i in range(l):
            if arr[i]=='(':
                if openn==0:
                    arr[i]=''
                openn+=1
            else:
                if openn==1:
                    arr[i]=''
                openn-=1
        res = ''.join(arr)
        return res