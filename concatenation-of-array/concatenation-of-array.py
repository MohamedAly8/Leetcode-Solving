class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        numlen = len(nums)

        for i in range(numlen):

            nums.append(nums[i])
        
        return nums
        



