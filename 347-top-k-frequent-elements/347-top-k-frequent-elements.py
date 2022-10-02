class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Add elements into hash
        counts = {}        
        freq = [[] for i in range(len(nums)+1)]
        # [[], [], [], [], [], [] ]      
        
        
        # have the counts
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
              
                
        for num, count in counts.items():
    
            freq[count].append(num)
        
        # k = 2
        out = []
        for i in range(len(freq)-1,0,-1):
            
            for num in freq[i]:
                if k > 0:
                    out.append(num)
                    k -= 1
        return out
        
            