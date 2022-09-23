class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # pointer at 1 -> N
        prefix = ""
        
        if len(strs) == 0:
            return prefix
        
        for i in range(len(min(strs))):
            char = strs[0][i]
            
            if all(a[i] == char for a in strs):
                prefix += char
            else:
                break
        return prefix