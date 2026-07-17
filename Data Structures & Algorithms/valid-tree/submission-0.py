class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {i : [] for i in range(n)}
        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)

            for neigh in nodes[curr]:
                if neigh == prev:
                    continue
                if not dfs(neigh, curr):
                    return False
            
            return True

        return dfs(0 ,-1)  and len(visited) == n