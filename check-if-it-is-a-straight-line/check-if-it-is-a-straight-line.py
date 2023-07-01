class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if (x2-x1) != 0:
            m = (y2-y1) / (x2-x1)
        else:
            m = -1
        b = y2 - (m*x2)

        print(m)

        for x,y in coordinates[2:]:

            # vertical line
            if m == -1:
                if x != x1:
                    print(x, x1)
                    return False

            elif y != (x*m+b):
                print("here")
                return False

        return True

