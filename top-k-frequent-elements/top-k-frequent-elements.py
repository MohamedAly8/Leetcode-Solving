class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # 1) coutn each number
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            
            counts[num] = counts.get(num,0) + 1

        
        for n,count in counts.items():
            freq[count].append(n)

        
        for i in range(len(freq)-1,-1,-1):

            for num in freq[i]:
                res.append(num)
            
            if len(res) == k:
                return res

        





        
            