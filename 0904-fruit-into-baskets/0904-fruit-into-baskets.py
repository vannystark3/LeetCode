class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        l = len(fruits)
        c = 0
        d = {}
        maxi=0
        for right in range(l):
            if fruits[right] not in d:
                d[fruits[right]] = 1
            else:
                d[fruits[right]] += 1
            c += 1
            if len(d.values())>2 and left<l:
                d[fruits[left]] -= 1
                if d[fruits[left]]==0:
                    del d[fruits[left]]
                left += 1
                c-=1
            maxi = max(maxi,c)
        return maxi