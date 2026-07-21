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
        
        taken = set()
        while q:
            c = q.popleft()
            if len(courseAndPre[c]) == 0:
                # all prereq for c satisfied, take c
                taken.add(c)
                for nxt in preAndCourse[c]:
                    # c is satisfied for dependent classes
                    if c in courseAndPre[nxt]:
                        courseAndPre[nxt].remove(c)
                    q.append(nxt)
        
        return len(taken) == numCourses
        
