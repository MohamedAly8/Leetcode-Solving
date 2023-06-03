class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # [2,3,6,7]
        res = []
        # DFS on each character adding the current index and i+1 index
        def dfs(i, cursum, cur):

            print(i,cursum,cur)

            if cursum == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or cursum > target:
                return 
            
            # DFS on current index
            cur.append(candidates[i])
            dfs(i,cursum+candidates[i],cur)

            cur.pop()
            # DFS on next index
            dfs(i+1,cursum, cur)

        dfs(0,0,[])
        return res
