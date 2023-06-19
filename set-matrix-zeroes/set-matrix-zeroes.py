class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        visitedROWS = set()
        visitedCOLS = set()

        for i in range(ROWS):
            for j in range(COLS):
                
                # already marked
                if i in visitedROWS and j in visitedCOLS:
                    continue 

                if matrix[i][j] == 0:
                    visitedROWS.add(i)
                    visitedCOLS.add(j)
    
        print(visitedROWS)
        print(visitedCOLS)

        for row in visitedROWS:
            for i in range(len(matrix[row])):
                matrix[row][i] = 0

        for col in visitedCOLS:
            for i in range(len(matrix)):
                matrix[i][col] = 0


        


            
                


