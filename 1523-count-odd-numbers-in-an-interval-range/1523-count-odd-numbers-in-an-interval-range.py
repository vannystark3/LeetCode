class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        res = diff//2
        if high%2!=0 or low%2!=0:
            res+=1
        return res