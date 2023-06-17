class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)


        while left < right and top < bottom:

            # go from left to right on top row
            for i in range(left,right):
                res.append(matrix[top][i])
            
            top += 1
            # go from top to down on right col
            for i in range(top,bottom):
                res.append(matrix[i][right-1])

            right -= 1


            # SINCE NOW WE ARE GOING IN REVERSE ORDER
            # NEED THIS CHECK
            if not (left < right and top < bottom):
                break
            
            # go from right to left on botttom row 
            for i in range(right-1,left-1, -1):
                res.append(matrix[bottom-1][i])

            bottom -= 1
            # go from bottom to top row on left col
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left += 1
        

        return res