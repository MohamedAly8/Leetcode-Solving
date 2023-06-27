class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        MARK = "D"



        def dfs(r,c):

            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return

            board[r][c] = MARK

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]

            for d in dirs:
                i,j = d
                dfs(r+i, c+j)


        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c] == "O":
                    dfs(r,c)

        
        # turn all O to X
        for r in range(ROWS):
            for c in range(COLS):           
                if board[r][c] == "O":
                    board[r][c] = "X"

        # turn O to D
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "D":
                   board[r][c] = "O"



