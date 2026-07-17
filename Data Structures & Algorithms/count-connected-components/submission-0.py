class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i : [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0

        def dfs(i):
            visited.add(i)
            for neigh in adj[i]:
                if neigh not in visited:
                    dfs(neigh)

        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count