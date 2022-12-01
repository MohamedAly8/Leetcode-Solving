class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])        
        
        new_ints = []
        
        s = intervals[0][0]
        e = intervals[0][1]
        i = 1
        while i < len(intervals):
            
        
            if intervals[i][0] <= e:
                # merge needed, contained
                e = max(e, intervals[i][1])
            
            else:
                new_ints.append([s,e])
                s,e = intervals[i][0], intervals[i][1]           
            i += 1
        
        
        new_ints.append([s,e])
        
        return new_ints