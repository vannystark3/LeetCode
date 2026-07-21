class Solution:
    def check(self,matrix):
        if matrix[0][0]==matrix[1][1]==matrix[2][2]!=None:
            return matrix[0][0]
        elif matrix[0][2]==matrix[1][1]==matrix[2][0]!=None:
            return matrix[0][2]
        elif matrix[0][0]==matrix[0][1]==matrix[0][2]!=None:
            return matrix[0][0]
        elif matrix[1][0]==matrix[1][1]==matrix[1][2]!=None:
            return matrix[1][0]
        elif matrix[2][0]==matrix[2][1]==matrix[2][2]!=None:
            return matrix[2][0]
        elif matrix[0][0]==matrix[1][0]==matrix[2][0]!=None:
            return matrix[0][0]
        elif matrix[0][1]==matrix[1][1]==matrix[2][1]!=None:
            return matrix[0][1]
        elif matrix[0][2]==matrix[1][2]==matrix[2][2]!=None:
            return matrix[0][2]
        return None
    def tictactoe(self, moves: List[List[int]]) -> str:
        l = len(moves)
        matrix = [[None for _ in range(3)] for _ in range(3)]
        flag = True
        for i in range(l):
            x,y = moves[i]
            mark = 'X' if flag else 'O'
            flag = not flag
            matrix[x][y] = mark
        
        res = self.check(matrix)
        if res is not None:
            return 'A' if res=='X' else 'B'
        if l==9:
            return "Draw"
        return "Pending"

        