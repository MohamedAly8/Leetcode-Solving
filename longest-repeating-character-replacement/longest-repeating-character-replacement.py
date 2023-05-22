class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # limited to A-Z


        # substring is valid of there are at most K replacements
            # replace char that occurs less frequent 

        # hashmap count -> "AABABBA"
        count = {}

        maxCount = 0

        start = 0

        ret = 0

        for end in range(len(s)):

            # +1 to char
            count[s[end]] = 1 + count.get(s[end], 0)

            #update the highest count in the current window
            maxCount = max(maxCount, count[s[end]])

            # no longer valid
            if(end - start + 1) - maxCount > k:

                # take out the last char from dictionary
                count[s[start]] -= 1

                # take out last char from window
                start += 1
            
            ret = max(ret, end - start + 1)
        
        return ret




