class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxW = 0
        
        p1 = 0
        p2 = len(height) - 1 
        
        while p1 < p2:
            
            currW = min(height[p1], height[p2]) * (p2 - p1)
            
            if currW > maxW:
                maxW = currW
                
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        return maxW
             