class Solution:
    def upper_bound(self,presum,curr,l):
        i,j = 0,l
        while i<j:
            mid = (i+j)//2
            if presum[mid]<=curr:
                i = mid+1
            else:
                j = mid
        return i
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        ans = []
        presum = []
        sums = 0
        for task in tasks:
            sums += task
            presum.append(sums)
        total = presum[-1]
        l = len(presum)

        curr = 0
        for shift in shifts:
            curr+=shift
            if curr>=total:
                ans.append(0)
                curr=0
            else:
                a = self.upper_bound(presum,curr,l)
                ans.append(l-a)
        return ans