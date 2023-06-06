class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adjList = defaultdict(list)

        for course,pre in prerequisites:
            adjList[course].append(pre)

        # now adj list has [course] :-> [prerequisits]
        curr_path = set()

        def dfs(course):
            # DFS on each courses till base case reached (no prereq)

            # cycle detected
            if course in curr_path:
                return False

            if adjList[course] == []:
                # no prereqs
                return True

            
            curr_path.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            curr_path.remove(course)
            # can label is as good to save time
            adjList[course] = []

            return True    
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True


