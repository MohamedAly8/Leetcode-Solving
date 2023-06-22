class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       
        # Creating a set to store the last positions of occurrence
        seen = set()
        res = 0
        start = 0
        
        for end in range(len(s)):

            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            res = max(res, end-start+1)
    
        return res



            
               