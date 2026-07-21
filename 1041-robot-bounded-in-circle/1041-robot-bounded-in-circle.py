class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        currdir = 'N'
        L = {"N":"W","W":"S","S":"E","E":"N"}
        R = {"N":"E","E":"S","S":"W","W":"N"}
        i = 0
        while i<4:
            for instruction in instructions:
                if instruction=='G':
                    if currdir=='N':
                        pos[1] += 1
                    elif currdir=='S':
                        pos[1] -= 1
                    elif currdir=='E':
                        pos[0] += 1
                    else:
                        pos[0] -= 1
                elif instruction=='L':
                    currdir = L[currdir]
                else:
                    currdir = R[currdir]
            i += 1
        return pos==[0,0]