class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1
        alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
        dic = {}
        
        for char in alphanum:
            dic[char] = 1
        s = s.lower()

        
    
        
        
        while start < end:
            
            if s[start] in dic.keys() and s[end] in dic.keys():
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            elif s[start] in dic.keys():
                end -= 1 
            elif s[end] in dic.keys():
                start += 1
            else:
                start += 1
                end -= 1
            
        return True