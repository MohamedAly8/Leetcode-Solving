class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {')':'(', ']':'[', '}':'{'}

        for b in s:
            
            
            if b not in brackets:
                stack.append(b)
                continue
            
            if not stack or brackets[b] != stack.pop():
                return False
                    
        
        return not stack