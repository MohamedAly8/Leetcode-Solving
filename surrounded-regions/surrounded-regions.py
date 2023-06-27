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

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c] == "O":
                    dfs(r,c)

        
        # turn all O to X, turn all D to O
        for r in range(ROWS):
            for c in range(COLS):           
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                   board[r][c] = "O"




