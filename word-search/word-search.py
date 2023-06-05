class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        if not board or not board[0]:
            return False


        visited = set()
        m, n = len(board), len(board[0])

        def dfs(subword, r, c):

            # print("new dfs on ", subword, "at r,c",r,c)

            if subword == "":
                return True

            if r not in range(m) or c not in range(n) or (r,c) in visited or subword[0] != board[r][c]:
                return False
            
            nsw = subword[1:]
            visited.add((r,c))

            res = dfs(nsw, r+1,c) or dfs(nsw, r-1,c) or dfs(nsw, r, c+1) or dfs(nsw, r, c-1)
            visited.remove((r,c)) 
            return res

        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(m):
            for c in range(n):
                if dfs(word,r,c):
                    return True
        return False