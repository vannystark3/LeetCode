class Solution:
    def next(self,prev):
        new = [1]
        l = len(prev)
        for i in range(l-1):
            new.append(prev[i]+prev[i+1])
        new.append(1)
        return new

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        res = [[1],[1,1]]
        j = 2
        while j<numRows:
            j += 1
            new = self.next(res[-1])
            res.append(new)
        return res
