class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseAndPre = defaultdict(set)
        preAndCourse = defaultdict(set)
        for pre, cla in prerequisites:
            courseAndPre[cla].add(pre)
            preAndCourse[pre].add(cla)
        
        # find courses with no prereq
        q = deque()
        for c in range(numCourses):
            if len(courseAndPre[c]) == 0:
                q.append(c)
        
        taken = 0
        while q:
            c = q.popleft()
            if len(courseAndPre[c]) == 0:
                # all prereq for c satisfied, take c
                taken += 1
                for nxt in preAndCourse[c]:
                    # c is satisfied for dependent classes
                    courseAndPre[nxt].remove(c)
                    q.append(nxt)
        
        return taken == numCourses
        
