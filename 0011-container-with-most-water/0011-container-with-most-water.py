class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        maxi = 0
        while i<j:
            start,end = height[i],height[j]
            area = min(start,end)*(j-i)
            maxi = max(area,maxi)
            if start<end:
                i += 1
            else:
                j -= 1
        return maxi