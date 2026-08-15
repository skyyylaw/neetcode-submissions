class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = {}
        def hasWC():
            counts = list(counter.values())
            counts.sort()
            return sum(counts[:-1]) <= k

        
        ans = 0
        
        left = 0
        right = left
        i = 1
        while right < len(s):
            
            if s[right] not in counter:
                counter[s[right]] = 0
            counter[s[right]] += 1


            while not hasWC():
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1

            ans = max(ans, right - left + 1)

            right += 1
        return ans