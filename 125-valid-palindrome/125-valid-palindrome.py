class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1
        alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
        dic = dict(enumerate(alphanum))
        s = s.lower()
        print(dic.values())
        print(s[start])
        print(s[start] in dic.values())
        
        
    
        
        
        while start < end:
            
            if s[start] in dic.values() and s[end] in dic.values():
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            elif s[start] in dic.values():
                end -= 1 
            elif s[end] in dic.values():
                start += 1
            else:
                start += 1
                end -= 1
            
        return True