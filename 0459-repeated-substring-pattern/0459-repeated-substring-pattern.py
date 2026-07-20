class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new = s+s
        new = new[1:-1]
        if s in new:
            return True
        return False