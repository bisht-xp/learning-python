def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    check_courses = {i: [] for i in range(len(numCourses))}
    for course, pre in prerequisites:
        check_courses[course].append(pre)

    visited = set()
    def dfs(crs):
        if crs in visited:
            return False

        visited.add(crs)
        for c in check_courses[crs]:
            if not dfs(c):
                return False
        
        visited.remove(crs)
        check_courses[crs] = []
        return True
    
    for n in range(numCourses):
        if not dfs(n):
            return False
        

    return True