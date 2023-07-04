class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        l = r = 0
        ans = 0
        while r < len(nums):
            if nums[r] > threshold:
                l = r+1
            elif r != l and nums[r] % 2 == nums[r-1] % 2:
                l = r
            while l <= r and nums[l] % 2:
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans