class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
    
    
        mSum = 0
        
        for i in range(1,len(nums)):
            
            currSum = 0
            while(i < len(nums) and nums[i-1] < nums[i]):
                currSum += 1
                i += 1
                
            mSum = max(mSum, currSum)
    
        return mSum + 1