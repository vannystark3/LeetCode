class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev = 0
        prev2 = 1
        for i in range(2,n+1):
            nexti = prev+prev2
            print(nexti)
            prev = prev2
            prev2 = nexti
        return prev2
