class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        def checkUnique(nums):

            print(nums)

            s = set()

            for num in nums:
                if num == '.':
                    continue
                if num in s:
                    print("here")
                    return False
                s.add(num)
            return True

        for line in board:

            # If checkUnique returns False
            if not checkUnique(line):
                return False


        # check all verticals 
        for i in range(9):
            vert = [board[x][i] for x in range(9)]

            if not checkUnique(vert):
                return False    

        # Check boxes 3x3

        for i in range(0,9,3):
            for j in range(0,9,3):

                box = [board[i][j+x] for x in range(3)]
                box2 = [board[i+1][j+x] for x in range(3)]
                box3 = [board[i+2][j+x] for x in range(3)]
                res = box + box2 + box3

                if not checkUnique(res):
                    return False

        return True
        
    