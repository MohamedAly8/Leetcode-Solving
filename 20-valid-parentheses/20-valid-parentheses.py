class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {')':'(', ']':'[', '}':'{'}

        for b in s:
            
            
            if b in brackets.values():
                stack.append(b)
        
            elif b in brackets.keys():
                
                if len(stack) != 0:
                    if brackets[b] != stack.pop():
                        return False
                else:
                    return False
                    
        
        if len(stack) == 0:
            return True
        return False