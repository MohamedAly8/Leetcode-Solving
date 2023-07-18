class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # monotonic decreasing order stack
        stack = []
        res = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                curtemp, index = stack.pop()
                res[index] = i - index
            
            stack.append([temp,i])

        return res



            



