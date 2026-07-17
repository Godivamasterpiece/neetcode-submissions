class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        crs = {i: [] for i in range(numCourses)}

        for cr, preq in prerequisites:
            crs[cr].append(preq)

        visited = set()        
        self.courses_ordered = []

        def dfs(cr):
            if cr in visited:
                return False

            if cr in self.courses_ordered:
                return True
            
            visited.add(cr)

            for pre in crs[cr]:
                if not dfs(pre): return False

            visited.remove(cr)
            self.courses_ordered.append(cr)

            return True


        for c in range(numCourses):
            if not dfs(c):
                return []

        return self.courses_ordered