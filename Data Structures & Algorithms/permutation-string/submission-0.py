class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for e in s1:
            counter[e] += 1
        
        left = 0
        for right in range(len(s2)):
            while left <= right and (s2[right] not in counter or counter[s2[right]] == 0):
                if s2[left] in counter:
                    counter[s2[left]] += 1
                left += 1
            if s2[right]  in counter and counter[s2[right]] > 0:
                counter[s2[right]] -= 1
            if right - left + 1 == len(s1):
                return True
        
        return False
            
