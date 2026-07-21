class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0,10:0}
        for bill in bills:
            if bill==5:
                d[5] += 1
            elif bill==10:
                d[10]+=1
                d[5]-=1
            else:
                if d[10]>0:
                    d[10]-=1
                    d[5]-=1
                else:
                    d[5]-=3
            if d[5]<0:
                return False
        return True