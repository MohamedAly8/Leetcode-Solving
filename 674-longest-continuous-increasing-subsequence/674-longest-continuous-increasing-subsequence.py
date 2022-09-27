class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        longest = 1
        mlen = 0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                longest += 1
            else:
                    mlen = max(longest,mlen)
                    longest = 1

        return max(mlen,longest)