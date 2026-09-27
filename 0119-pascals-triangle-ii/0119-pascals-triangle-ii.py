class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0:
            return [1]
        res = [1]
        val = 1
        for i in range(1,rowIndex+1):
            val = val*(rowIndex-i+1)//i
            res.append(val)
        return res            