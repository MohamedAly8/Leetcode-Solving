class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # vertical line
        if x1 == x2:
            for x,y in coordinates:

                if x != x1:
                    return False
            return True

        
        m = (y2-y1) / (x2-x1)
        b = y2 - m*x2

        for x,y in coordinates[2:]:
            if y != (m*x+b):
                return False
        return True
