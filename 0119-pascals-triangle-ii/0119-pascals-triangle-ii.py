class Solution:
    def next(self, prev):
        res = [1]
        l = len(prev)
        for i in range(1,l):
            res.append(prev[i-1]+prev[i])
        res.append(1)
        return res
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0:
            return [1]
        curr = [1]
        for i in range(rowIndex):
            curr = self.next(curr)
        return curr
        
        
            