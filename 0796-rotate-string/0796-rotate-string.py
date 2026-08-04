class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new = s+s
        if len(s)!=len(goal):
            return False
        if goal in new:
            return True
        return False