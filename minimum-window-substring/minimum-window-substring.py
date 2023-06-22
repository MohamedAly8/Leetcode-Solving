class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""


        countT = defaultdict(int)
        window = defaultdict(int)
        
        for c in t:
            countT[c] += 1
    
        have, need = 0, len(t) 
        res, res_count = [-1,-1], float('inf')

        start = 0
        for end in range(len(s)):

            curC = s[end]
            window[curC] += 1

            if curC in countT and window[curC] <= countT[curC]:
                have += 1
        
            while have == need:
                
                if (end-start+1 < res_count):
                    res = [start, end]
                    res_count = end-start+1

                window[s[start]] -= 1
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have -= 1

                start += 1

        start, end = res
                
    
        return s[start: end+1] if res_count != float('inf') else ""





        