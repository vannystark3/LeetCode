class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        l = len(salary)
        total = 0
        for i in range(1,l-1):
            total += salary[i]
        return total/(l-2)