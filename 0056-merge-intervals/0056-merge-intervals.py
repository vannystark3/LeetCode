class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        res = []
        i = 0
        start,end=-1,-1
        while i<l:
            currs,curre = intervals[i]
            if start==-1:
                start,end = currs,curre
            else:
                if currs<=end:
                    end = max(end,curre)
                else:
                    res.append([start,end])
                    start,end = currs,curre
            if i==l-1:
                res.append([start,end])
            i += 1
        return res
                