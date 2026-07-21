class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        i,j=0,0
        while i<n and j<n:
            total += mat[i][j]
            i += 1
            j += 1
        i,j = 0,n-1
        while i<n and j>=0:
            total += mat[i][j]
            i += 1
            j -= 1
        if n%2!=0:
            mid = n//2
            total -= (mat[mid][mid])
        return total