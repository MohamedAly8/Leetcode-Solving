class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # IDEA: keep count of all current elements in the window,


        #  keep track of max_freq element.


        count = defaultdict(int)

        l  = 0
        res = 0
        max_freq = 0

        for r in range(len(s)):

            count[s[r]] += 1
            
            max_freq = max(count[s[r]], max_freq)


            # too many 
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(r-l+1, res)

        return res














        


