class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        
        visitSet = set()

        def DFS(course, visit):
            if course in visit:
                return False
            if preMap[course] == []:
                return True

            visit.add(course)
            for preq in preMap[course]:
                if not DFS(preq, visit):
                    return False   
            
            visit.remove(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not DFS(i, visitSet):
                return False
        
        return True



            