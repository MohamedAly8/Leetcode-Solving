class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,3,4]
        prefix = []
        postfix = []    
    
        for i in range(len(nums)):
            prefix.append(1)
            postfix.append(1)
        
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i]
            
        return nums
            