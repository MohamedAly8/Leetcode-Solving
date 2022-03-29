class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,3,4]
        result = []
        p = 1
        result.append(p)        
        
        for i in range(1,len(nums)):
            p = nums[i-1] * p
            result.append(p)  
    
        p = 1
        for i in range(len(nums)-2, -1,-1):
            p = nums[i+1] * p
            result[i] *= p
    
                     
        return result
            