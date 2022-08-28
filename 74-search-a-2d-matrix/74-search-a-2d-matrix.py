class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    
        # List Midpoint
        l = 0
        h = len(matrix) - 1
        midPoint = h // 2
        
        
        while l <= h:
            
            if matrix[midPoint][0] == target:
                return True
            
            if matrix[midPoint][0] > target:
                h = midPoint - 1
                midPoint = (l+h) // 2
            
            else:
                l = midPoint + 1
                midPoint = (l+h) // 2
                
            
        toFind = matrix[midPoint]
        # Binary Search on matrix
        print(toFind)
        
        l = 0
        h = len(toFind) - 1
        midPoint = h // 2
        
                
        while l <= h:
            print("here")
            print(toFind[midPoint])
            
            if toFind[midPoint] == target:
                return True
            
            if toFind[midPoint] > target:
                h = midPoint - 1
                midPoint = (l+h) // 2
            
            else:
                l = midPoint + 1
                midPoint = (l+h) // 2
                
        return False
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        