class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

                # The total number of cookies
        n = len(cookies)

        # An array to store the number of cookies each child currently has
        children = [0]*k
        
        # Sort the cookies array in descending order
        # We start with the bag with the most cookies to help with pruning
        cookies.sort(reverse=True)

        # The minimum unfairness so far. Initialized to infinity
        min_unfairness = float('inf')
        
        # Define the recursive function
        def backtrack(i):
            nonlocal min_unfairness

            # Base case: if all bags have been distributed
            if i == n:
                # Update min_unfairness
                min_unfairness = min(min_unfairness, max(children))
                return

            # Iterate over all children
            for j in range(k):
                # Assign the ith bag to the jth child
                children[j] += cookies[i]

                # Prune the search space if the max cookies a child has is 
                # already greater than min_unfairness
                if max(children) < min_unfairness:
                    backtrack(i+1)

                # Undo the assignment (backtrack)
                children[j] -= cookies[i]

        # Start the backtracking
        backtrack(0)

        return min_unfairness