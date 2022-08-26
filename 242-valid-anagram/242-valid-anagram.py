class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic = {}
        
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
            
            
        for letter in t:
            if letter in dic.keys() and dic[letter] >= 1:
                dic[letter] -= 1
            else:
                return False
        return True