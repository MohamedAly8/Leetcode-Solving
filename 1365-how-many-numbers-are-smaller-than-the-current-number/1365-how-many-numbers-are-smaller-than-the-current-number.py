class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
        nums_sorted = sorted(nums)
        return (nums_sorted.index(a) for a in nums)