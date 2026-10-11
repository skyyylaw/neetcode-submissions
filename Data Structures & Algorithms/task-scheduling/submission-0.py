class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        q = [(0, -d[k]) for k in d]
        heapq.heapify(q)
        time = 0
        while q:
            print(q, time)
            if time < q[0][0]:
                time += 1 
                continue
            earliest_start, task_count = heapq.heappop(q)
            task_count += 1
            if task_count != 0:
                next_earliest_start = time + n + 1
                heapq.heappush(q, (next_earliest_start, task_count))
            time += 1
        return time