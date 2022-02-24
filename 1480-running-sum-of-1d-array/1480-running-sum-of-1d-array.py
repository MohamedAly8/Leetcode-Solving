class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sum_before = 0
        lst = []
        
        # [1,2,3,4]
        #
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
            