class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1,el2 = -1,-1
        c1,c2 = 0,0
        l = len(nums)//3
        for num in nums:
            if num==el1:
                c1+=1
            elif num==el2:
                c2+=1
            elif c1==0:
                c1 = 1
                el1 = num
            elif c2==0:
                c2 = 1
                el2 = num
            else:
                c1 -= 1
                c2 -= 1
        c1,c2 = 0,0
        for num in nums:
            if num==el1:
                c1+=1
            elif num==el2:
                c2+=1
        res = []
        if c1>l:
            res.append(el1)
        if c2>l:
            res.append(el2)
        return res

