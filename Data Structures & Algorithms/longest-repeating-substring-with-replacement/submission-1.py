class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        def maxicha():
            res = ""
            count = 0
            for cha in counter:
                if counter[cha] > count:
                    count = counter[cha]
                    res = cha
            return res

        length = 0
        for l in range(len(s)):
            while l + length < len(s) and (len(counter) == 1 or s[l+length] == maxicha() or length - counter[maxicha()] < k):
                counter[s[l+length]] += 1
                length += 1
            counter[s[l]] -= 1
            if counter[s[l]] == 0: 
                counter.pop(s[l])
        
        return length


                