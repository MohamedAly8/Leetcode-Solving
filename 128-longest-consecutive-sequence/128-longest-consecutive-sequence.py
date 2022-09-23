class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_list = sorted(nums)
        
        max_longest = 1
        longest = 1
        

        
        for i in range(len(sorted_list)-1):
            if(sorted_list[i+1] == sorted_list[i]):
                continue
            if(sorted_list[i+1] == sorted_list[i] + 1):
                longest += 1
            else:
                longest = 1
            if longest >= max_longest:
                max_longest = longest
            
        
        if len(nums) == 0:
            return 0
        
        return max_longest

            
        
        
        # [ 0,0,1,2,3,4,5,6,7,8]