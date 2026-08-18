class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        lsum = sum(cardPoints[:k])
        maxi = lsum
        left=k-1
        right=l-1
        c=0
        rsum = 0
        while c<k:
            lsum -= cardPoints[left]
            rsum += cardPoints[right]
            maxi = max(maxi,lsum+rsum)
            left -= 1
            right -= 1
            c+=1
        return maxi