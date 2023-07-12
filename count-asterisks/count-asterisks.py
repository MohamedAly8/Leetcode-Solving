class Solution:
    def countAsterisks(self, s: str) -> int:

        add = True
        res = 0

        for c in s:

            if c == '|':
                add = not add
    
            if c == '*' and add:
                res += 1

        return res
        

    