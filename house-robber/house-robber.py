class Solution:
    def rob(self, nums: List[int]) -> int:


        h1 = 0
        h2 = 0

        for i in range(len(nums)):

            temp = max(nums[i]+h1, h2)
            h1 = h2
            h2 = temp

        return h2


            

            



            
        



        