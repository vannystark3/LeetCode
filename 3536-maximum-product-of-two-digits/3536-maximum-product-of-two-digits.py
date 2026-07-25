class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while n!=0:
            d = n%10
            arr.append(d)
            n = n//10
        arr.sort(reverse=True)
        print(arr)
        return arr[0]*arr[1]