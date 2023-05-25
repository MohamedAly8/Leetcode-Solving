class Solution:
    def rob(self, nums: List[int]) -> int:


        r = [0,0]
        
        r1 = 0
        r2 = 0


        for num in nums:

            temp = r2

            r2 = max(num+r1, r2)
            r1 = temp 

            # r.append(max(temp, r[-1]))
            print(r1,r2)

        # print(r)

        return r2


            
        



        