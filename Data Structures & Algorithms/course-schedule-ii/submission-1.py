class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqFor = defaultdict(list)
        prereqCount = {}
        
        for i in range(numCourses):
            prereqCount[i] = 0
        
        for cla, pre in prerequisites:
            prereqFor[pre].append(cla)
            prereqCount[cla] += 1
        
        q = deque()
        for cla in prereqCount:
            if prereqCount[cla] == 0:
                q.append(cla)
        
        output = []

        while q:
            class_ = q.popleft()
            output.append(class_)
            for e in prereqFor[class_]:
                prereqCount[e] -= 1
                if prereqCount[e] == 0:
                    q.append(e)

        return [] if len(output) != numCourses else output
            