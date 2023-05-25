class Solution:
    def rob(self, nums: List[int]) -> int:


        r = [0,0]
        
        for num in nums:

            temp = num + r[-2]

            r.append(max(temp, r[-1]))

        print(r)

        return r[-1]


            
        



        