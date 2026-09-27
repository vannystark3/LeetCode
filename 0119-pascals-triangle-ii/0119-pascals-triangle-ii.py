class Solution:
    def next(self, prev):
        res = [1]
        l = len(prev)
        for i in range(1,l):
            res.append(prev[i-1]+prev[i])
        res.append(1)
        return res
    def getRow(self, rowIndex: int) -> list[int]:
        arr = [[1],[1,1]]
        for i in range(1,rowIndex):
            res = self.next(arr[-1])
            arr.append(res)
        return arr[rowIndex]
        
        
            