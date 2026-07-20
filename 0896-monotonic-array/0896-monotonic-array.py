class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = len(nums)
        if l==1:
            return True
        flag = None
        for i in range(l-1):
            if nums[i]>nums[i+1]:
                if flag is None:
                    flag=False
                elif flag is not False:
                    return False
            elif nums[i]<nums[i+1]:
                if flag is None:
                    flag=True
                elif flag is not True:
                    return False
        return True