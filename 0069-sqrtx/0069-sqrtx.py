class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        while l<=r:
            mid = l + (r-l)//2
            mul = mid*mid
            if mul == x:
                return mid
            elif mul>x:
                r = mid-1
            else:
                l = mid+1
        return r