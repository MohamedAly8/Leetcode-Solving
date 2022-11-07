class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        noLoss = []
        oneLoss = []
        
        dicW = {}
        dicL = {}
        for winner, loser in matches:
            dicL[loser] = dicL.get(loser,0) + 1
            dicW[winner] = dicW.get(winner,0)
            
        for k,v in dicL.items():
            
            if v == 1:
                oneLoss.append(k)
            
        for k,v in dicW.items():
            
            if k not in dicL.keys():
                noLoss.append(k)
        
        
        
        return [sorted(noLoss), sorted(oneLoss)]
            