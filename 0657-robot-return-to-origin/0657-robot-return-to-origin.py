class Solution:
    def judgeCircle(self, moves: str) -> bool:
        robo = [0,0]
        for move in moves:
            if move=='U':
                robo[0]+=1
            elif move=='D':
                robo[0]-=1
            elif move=='L':
                robo[1]+=1
            else:
                robo[1]-=1
        return robo==[0,0]