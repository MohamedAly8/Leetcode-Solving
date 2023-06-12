class Solution:
    def fib(self, n: int) -> int:

        n0 = 0
        n1 = 1
        res = 0

        if n < 2:
            return n

        for i in range(1,n):
            res = n0 + n1
            n0 = n1
            n1 = res
        
        return res