class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:


        index = 0
        count = 0


        if ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
    

        for i in range(len(items)):

            if items[i][index] == ruleValue:
                count += 1
        
        return count
                