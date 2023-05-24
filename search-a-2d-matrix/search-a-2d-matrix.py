class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


    
        # find correct row 

        s = 0
        e = len(matrix)-1

        m_r = (s+e) // 2
        found_row = False

        while s <= e:


            m_r = (s+e) // 2

            if target < matrix[m_r][0]:
                e = m_r - 1
            elif target > matrix[m_r][-1]:
                s = m_r + 1
            else:
                break


        if not (s <= e ):
            return False

        row = matrix[m_r]

        s = 0
        e = len(row)

        while s <= e:

            m = (s+e) // 2

            if target == row[m]:
                return True
            
            elif target > row[m]:
                s = m + 1
            
            else:
                e = m - 1
            
        return False

            
        








