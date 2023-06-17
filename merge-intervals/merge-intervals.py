class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []

        curInterval = intervals[0]

        for interval in intervals[1:]:

            if interval[0] > curInterval[1]:
                res.append(curInterval)
                curInterval = interval
            
            else:
                curInterval = [min(curInterval[0], interval[0]), max(curInterval[1], interval[1])]
        

        
        res.append(curInterval)
        return res
