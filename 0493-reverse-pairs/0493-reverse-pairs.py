class Solution:
    def merge(self,nums,l,mid,r):
        left,right = l,mid+1
        res = []
        while left<=mid and right<=r:
            if nums[left]<=nums[right]:
                res.append(nums[left])
                left += 1
            else:
                res.append(nums[right])
                right += 1
        while left<=mid:
            res.append(nums[left])
            left+=1
        while right<=r:
            res.append(nums[right])
            right+=1
        for i in range(l,r+1):
            nums[i] = res[i-l]
    def count(self,nums,l,mid,r):
        right = mid+1
        c = 0
        for i in range(l,mid+1):
            while right<=r and nums[i]>2*nums[right]:
                right+=1
            c+=(right-(mid+1))
        return c
    def mergeSort(self,nums,l,r):
        c = 0
        if l==r:
            return c
        mid = (l+r)//2
        c += self.mergeSort(nums,l,mid)
        c += self.mergeSort(nums,mid+1,r)
        c += self.count(nums,l,mid,r)
        self.merge(nums,l,mid,r)
        return c
    def reversePairs(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = self.mergeSort(nums,l,r)
        return res