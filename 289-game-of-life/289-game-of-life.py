class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        died = []
        aliv = []
        nbrs = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                alive = 0
                for x, y in nbrs:
                    dx = x+i
                    dy = y+j
                    if 0<=dx<len(board) and 0<=dy<len(board[0]) and board[dx][dy] == 1:
                        alive+=1
                if value == 0 and alive == 3:
                    aliv.append([i,j])
                elif value ==1 and (alive<2 or alive >3):
                    died.append([i,j])
        for i,j in died:
            board[i][j] = 0
        
        for i,j in aliv:
            board[i][j] = 1
            
        