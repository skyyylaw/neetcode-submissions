from _heapq import heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        
        ineligibleProjects = []
        eligibleProjects = []

        currCapital = w
        completedProjects = 0
        
        for i in range(n):
            if capital[i] <= currCapital:
                heapq.heappush(eligibleProjects, (-profits[i]))
            else:
                heapq.heappush(ineligibleProjects, (capital[i], profits[i]))
            
        while eligibleProjects and completedProjects < k:
            p = heapq.heappop(eligibleProjects)
            currCapital += -1 * p
            completedProjects += 1
            while ineligibleProjects and ineligibleProjects[0][0] <= currCapital:
                heapq.heappush(eligibleProjects, -heapq.heappop(ineligibleProjects)[1])
        
        return currCapital
