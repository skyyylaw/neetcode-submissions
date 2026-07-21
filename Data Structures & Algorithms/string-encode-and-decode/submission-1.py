class Solution:

    def encode(self, strs: List[str]) -> str:
        separations = ["___"] * 100
        for i in range(len(strs)):
            str_len = len(strs[i])
            str_len_str =  str(str_len)
            separations[i] = str_len_str.rjust(3, "0")
        return "".join(separations) + "".join(strs)
    def decode(self, s: str) -> List[str]:
        separations = [s[i*3:i*3+3] for i in range(100)]
        strs = s[3*100: ]
        ans = []
        start = 0
        for end in separations:
            if end == "___":
                return ans
            ans.append(strs[start:start + int(end)])
            start = start + int(end)
        return ans

