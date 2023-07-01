class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        
        maxLeft = [height[0]]


        for i in range(1, len(height)):
            tmp = max(maxLeft[-1], height[i])
            maxLeft.append(tmp)

        
        maxRight = [height[-1]]

        for i in range(len(height)-2,-1,-1):
            tmp = max(maxRight[0], height[i])
            maxRight.insert(0, tmp)
        
        res = 0
        for i in range(len(height)):
            
            tmp = min(maxLeft[i], maxRight[i])
            
            if tmp - height[i] > 0:
                res += tmp - height[i]

        return res
        

        


