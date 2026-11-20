class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = defaultdict(int)
        for c in t:
            counter[c] += 1
        
        def matchedAll(): # O(1)
            for k in counter:
                if counter[k] > 0:
                    return False
            return True
        
        ans = None
        
        left = 0
        for right in range(len(s)):
            # print(left, right)
            if s[right] in counter:
                counter[s[right]] -= 1

            while left < right and (s[left] not in counter or counter[s[left]] < 0):
                if s[left] in counter and counter[s[left]] < 0:
                    counter[s[left]] += 1
                left += 1
            
            if matchedAll():
                if ans == None:
                    ans = [left, right + 1]
                ans = [left, right + 1] if right + 1 - left < ans[1] - ans[0] else ans
                
                counter[s[left]] += 1
                left += 1
        
        if ans == None:
            return ""

        return s[ans[0]: ans[1]]
                
