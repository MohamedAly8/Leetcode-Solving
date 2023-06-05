class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Map of course: prereq
        preAdjList = {i: [] for i in range(numCourses)}

        # fill in prerequisites
        for course,prereq in prerequisites:
            preAdjList[course].append(prereq)


        # initialize visited 
        visited = set()

        # DFS, if cycle found return False
        def dfs(crs):

            # found cycle
            if crs in visited:
                return False
            
            # if reached base course
            if preAdjList[crs] == []:
                return True
            
            # add to visited list
            visited.add(crs)

            # loop through all prereqs and if any dfs return False, that means there's a cycle
            for prereq in preAdjList[crs]:
                if not dfs(prereq):
                    return False
            
            # there are no cycles for this course, remove path from visited
            visited.remove(crs)

            # make AdjList empty to save on computing
            preAdjList[crs] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


            


        return True