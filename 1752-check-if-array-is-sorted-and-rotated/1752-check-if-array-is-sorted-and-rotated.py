class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = 0
        l = len(nums)
        for i in range(l-1):
            if(nums[i+1]<nums[i]):
                t += 1
        if(t==1 and nums[l-1]<=nums[0]):
            return True
        elif(t==0):
            return True
        else:
            return False
        