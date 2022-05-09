class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
                    
        nbrs = [[0,1],[0,-1],[1,0],[-1,0]]           
        def dfs(i,j, fro, to):
            board[i][j] = to
            for x,y in nbrs:
                if 0<=i+x<len(board) and 0<=j+y<len(board[0]) and board[i+x][j+y] == fro:
                    dfs(i+x, j+y,fro,to)
                    
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i,j,'O','Y')
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == "O":
                    dfs(i,j,'O','Y')
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == 'O':
                    board[i][j] = 'X'
                elif value == 'Y':
                    board[i][j] = 'O'
        