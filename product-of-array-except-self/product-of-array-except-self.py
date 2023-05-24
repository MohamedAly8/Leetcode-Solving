class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        
        res = [1] * (len(nums))

        # multiply by all the numbers to the left of the number
        leftmult = 1

        for i in range(len(nums)):
            res[i] = leftmult
            
            leftmult *= nums[i]

            
        # right mult
        
        rightmult = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= rightmult
            rightmult *= nums[i]


        return res