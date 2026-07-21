class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        dx = x2-x1
        dy = y2-y1
        l = len(coordinates)
        for i in range(2,l):
            x,y = coordinates[i]
            if dx*(y-y2)!=dy*(x-x2):
                return False
            x2,y2 = x,y
        return True