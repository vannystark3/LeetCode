class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = 0
        for ch in num1:
            m = m*10 + ord(ch)-ord('0')
        n = 0
        for ch in num2:
            n = n*10 + ord(ch)-ord('0')
        return str(m*n)