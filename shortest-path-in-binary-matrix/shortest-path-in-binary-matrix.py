class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        # DFS Failed, need BFS

        n = len(grid)

        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append([0,0,1])
        grid[0][0] = 1

        while q:
            print("hello")
            r,c,dist = q.popleft()

            # reached end
            if (r,c) == (n-1,n-1):
                return dist
            
            for dx,dy in [(1,0),(1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]:
                rx, cy = r+dx, c+dy

                if rx in range(n) and cy in range(n) and grid[rx][cy] == 0:
                    q.append([rx,cy,dist+1])
                    grid[rx][cy] = 1

        return -1





