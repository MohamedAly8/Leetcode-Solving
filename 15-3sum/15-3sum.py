class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        # Target -> 0
        # [-1 , 0,  1, 2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        out = []
        
        for i, a in enumerate(nums):
            
            if i > 0 and a == nums[i - 1]:
                continue
        
        
            l, u = i + 1, len(nums) - 1
            
            while(l <  u):
                
                threeSum = a + nums[l] + nums[u]
                
                if threeSum > 0:
                    u -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    out.append([a, nums[l], nums[u]])
                    
                    l += 1
                    while(l < u and nums[l] == nums[l-1]):
                        l += 1
                    
        return out
                
                
                    
        