class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = len(grid)
        n = l*l
        nsum = n*(n+1)//2
        arrsum = 0
        nsq = n*(n+1)*((2*n)+1)//6
        arrsq = 0
        for vals in grid:
            for num in vals:
                arrsum += num
                arrsq += (num*num)
        val1 = nsum-arrsum
        val2 = nsq-arrsq
        val3 = val2//val1
        print(val1,val2,val3)
        x = (val1+val3)//2
        y = val3-x
        return [y,x]