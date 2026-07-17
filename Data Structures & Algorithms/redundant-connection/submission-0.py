class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        for u, v in edges:
            rootU, rootV = find(u), find(v)

            if rootU == rootV:
                return [u,v]

            parent[rootU] = rootV