class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = defaultdict(list)
        
        for crs, preq in prerequisites:
            preqMap[crs].append(preq)
        


        visited = set()

        def dfs(c):
            if c in visited:
                return False

            if not preqMap[c]:
                return True
            
            visited.add(c)

            for p in preqMap[c]:
                if not dfs(p):
                    return False
            
            visited.remove(c)
            preqMap[c] = []
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True