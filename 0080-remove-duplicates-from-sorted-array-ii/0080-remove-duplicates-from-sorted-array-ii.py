class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 1 # count 
        innercount = 1 # count how many occurances
        
        
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:
                innercount += 1

                if innercount > 2:
                    continue
            
            else:
                innercount = 1
            
            
            nums[count] = nums[i]
            count += 1    
        return count
            