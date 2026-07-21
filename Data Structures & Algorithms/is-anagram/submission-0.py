class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
            if counter[c] == -1:
                return False
            if counter[c] == 0:
                counter.pop(c)
        return len(counter) == 0