class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        def satisfied():
            for e in target:
                if target[e] > 0:
                    return False
            return True

        for c in t:
            target[c] += 1

        l = 0
        ans = "*" * (len(s)+1)
        for r in range(len(s)):
            if s[r] in target:
                target[s[r]] -= 1
            # print(s[l:r+1], satisfied())
            while satisfied():
                ans = s[l:r+1] if len(ans) > len(s[l:r+1]) else ans
                if s[l] in target:
                    target[s[l]] += 1
                l += 1
        return ans if ans != "*" * (len(s)+1) else ""