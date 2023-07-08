class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hash with value set as empty list
        ans = collections.defaultdict(list)

        for s in strs:

            crs = [0] * 26

            for c in s:
                crs[ord(c) - ord('a')] += 1
            
            ans[tuple(crs)].append(s)

        res = []
        for k in ans.keys():
            res.append(ans[k])

        return res
            

            


                 
