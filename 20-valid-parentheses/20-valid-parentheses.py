class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {')':'(', ']':'[', '}':'{'}

        for b in s:
            
            
            if b in brackets.values():
                stack.append(b)
        
            elif b in brackets.keys():
                
                if not stack or brackets[b] != stack.pop():
                    return False
                    
        
        return not stack