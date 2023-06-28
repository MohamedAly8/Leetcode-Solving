class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = defaultdict(list)
        queue = deque([start])

        #create adjacency list
        for i, (a,b) in enumerate(edges):

            graph[a].append([b,i])
            graph[b].append([a,i])

        
        # create probability list
        prob = [0.0] * n
        prob[start] = 1.0


        
        while queue:

            curr = queue.popleft()

            for neigh, i in graph.get(curr,[]):

                if prob[curr] * succProb[i] > prob[neigh]:
                    prob[neigh] = prob[curr] * succProb[i]
                    queue.append(neigh)
            
        return prob[end]

