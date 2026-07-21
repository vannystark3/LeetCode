class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for customer in accounts:
            allbanks = 0
            for money in customer:
                allbanks += money
            maxi = max(maxi,allbanks)
        return maxi
