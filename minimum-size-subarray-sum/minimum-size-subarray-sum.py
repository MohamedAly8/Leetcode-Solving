class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        res = float('inf')

        cursum = 0
        for r in range(len(nums)):


            cursum += nums[r]
            
            while cursum >= target and l <= r:

                res = min(res, r-l+1)
                cursum -= nums[l]
                l += 1


        return res if res != float('inf') else 0
            

            
            