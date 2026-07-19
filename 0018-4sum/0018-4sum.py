class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = len(nums)
        nums.sort()
        res = []
        for i in range(s):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,s):
                if (j!=(i+1)) and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = s-1
                while k<l:
                    sums = nums[i]+nums[j]+nums[k]+nums[l]
                    if sums==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k += 1
                        while k<l and nums[l]==nums[l+1]:
                            l -= 1
                    elif sums<target:
                        k += 1
                    else:
                        l -= 1
        return res
