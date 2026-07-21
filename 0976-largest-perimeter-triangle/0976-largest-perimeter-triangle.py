class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort(reverse=True)
        for i in range(l-2):
            a,b,c = nums[i],nums[i+1],nums[i+2]
            if (a+b)>c and (b+c)>a and (a+c)>b:
                return a+b+c
        return 0