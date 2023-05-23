class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # limited to A-Z
        # hashmap count -> "AABABBA"
        count = {}
        maxCount = 0
        start = 0
        ret = 0

        for end in range(len(s)):

            # add each letter to our counts
            count[s[end]] = count.get(s[end], 0) + 1

            # see if it is new most frequent
            maxCount = max(maxCount, count[s[end]])

            # overlimit
            if (end - start + 1) -  maxCount > k:
                count[s[start]] -= 1
                start += 1 
            
            ret = max(ret, end - start + 1)
            print("Start, end, ret", start,end, ret)
        
        return ret
            







        


