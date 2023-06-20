class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        s_i, t_i = 0, 0
        while t_i < len(t) and s_i < len(s):
            if s[s_i] == t[t_i]:
                s_i += 1    
            t_i += 1
    
        
        return s_i == len(s)
            
        
