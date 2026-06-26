class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxP = 0
        for num in prices:
            if num<=mini:
                mini = num
                continue
            else:
                maxP = max(maxP,num-mini)
        return maxP