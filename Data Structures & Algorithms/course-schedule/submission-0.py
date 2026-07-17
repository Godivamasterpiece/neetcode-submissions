class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = {i: [] for i in range(numCourses)}

        for crs, prs in prerequisites:
            mapping[crs].append(prs)

        visited_set = set()

        def dfs(crs):
            if crs in visited_set:
                return False

            if mapping[crs] == []:
                return True

            visited_set.add(crs)

            for pre in mapping[crs]:
                if not dfs(pre): return False

            visited_set.remove(crs)

            mapping[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True