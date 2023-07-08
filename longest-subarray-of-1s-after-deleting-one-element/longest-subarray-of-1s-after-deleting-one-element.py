class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zero = 0
        l = 0

        res = 0
        

        for r in range(len(nums)):

            
            if nums[r] == 0:
                print("added 0 at:", r)
                zero += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            
            print(l,r, "zeros:", zero)
            res = max(res, r-l)

        return res
            
