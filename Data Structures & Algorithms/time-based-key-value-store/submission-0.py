class TimeMap:

    def __init__(self):
        self.m = defaultdict(dict)
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        time = self.time[key]

        l = 0
        r = len(time) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp == time[mid] or (timestamp > time[mid] and (mid == len(time)-1 or timestamp < time[mid+1])):
                return self.m[key][time[mid]]
            elif timestamp < time[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return ''

        
