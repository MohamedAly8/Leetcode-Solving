class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        count = 0

        for i in range(1,len(nums)):

            # not increasing
            if nums[i] <= nums[i-1]:
                count += 1

                if count > 1:
                    return False
                
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]

        
        return True
