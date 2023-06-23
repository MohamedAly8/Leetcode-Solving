class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        # base case at last element LIS=1

        # LIS len-1 : 1 , or 1 + LIS[3] ONLY IF nums[len-1] < nums[len]

        dp = [1] * len(nums)  
        curMax = 1
    
        for i in range(len(nums)-1, -1, -1):

            j = i + 1
            while(j < len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
                    curMax = max(dp[i], curMax)
                j += 1                     
        return curMax

            