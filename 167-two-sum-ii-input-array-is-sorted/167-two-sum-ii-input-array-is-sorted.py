class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        begin = 0
        end = len(numbers) - 1
        
        while begin < end:
            
            currSum = numbers[begin] + numbers[end]
            
            if currSum == target:
                return [begin+1, end+1]
    
            elif currSum > target:
                end -= 1
            elif currSum < target:
                begin += 1
  
                
        return -1
        
        