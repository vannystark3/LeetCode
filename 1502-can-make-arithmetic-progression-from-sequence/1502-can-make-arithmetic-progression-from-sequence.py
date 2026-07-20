class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l = len(arr)
        for i in range(1,l-1):
            if (arr[i]-arr[i-1])!=(arr[i+1]-arr[i]):
                return False
        return True