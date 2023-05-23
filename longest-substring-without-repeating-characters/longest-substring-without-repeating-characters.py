class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       
        # Creating a set to store the last positions of occurrence
        seen = set()
        maximum_length = 0
    
        # starting the initial point of window to index 0
        start = 0
        
        # index of end of window
        for end in range(len(s)):

            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            print(start,end)
            seen.add(s[end])

            # we know it is unique
            maximum_length = max(end - start + 1, maximum_length)
        
        return maximum_length
            
               