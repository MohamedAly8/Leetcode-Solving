class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.l = [None for _ in range(n+1)]
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey] = value
        result = []

        while self.ptr <= self.n and self.l[self.ptr] is not None:
            result.append(self.l[self.ptr])
            self.ptr += 1
        return result



        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)