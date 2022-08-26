class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [1, 5 ,8, 12, 14]
        
        # target -> 65
        
        # 1) find midpoint
        
        low = 0
        high = len(nums)-1
        midpoint = (low + high) // 2
        
        
        
        # 2) check if target value is greater then or less then midpoint
        
        while low <= high:
                
            if target == nums[midpoint]:
                return midpoint

            elif target > nums[midpoint]:
                low = midpoint + 1 
                midpoint = (low + high) // 2

            elif target < nums[midpoint]:
                high = midpoint - 1
                midpoint = (low + high) // 2
                
            print(low, high)

        return -1

                    
        
        
#             # 2a) if greater than
#             delete the lesser half of the list 
            
#             # 2b) if less than
#             delete the greater half of the list 
#             # 2c) if equal
#             return midpoint
            
#         # 3) check. midpoint of the new list 
    
        
#         # 4) repeat step 2
        
#         # stops when the target value is found or when it is not found in the list 
        
        
        
        