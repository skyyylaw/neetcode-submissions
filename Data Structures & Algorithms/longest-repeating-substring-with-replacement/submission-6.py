class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        right = left
        wildcards = k

        i = 1
        while right < len(s):
            # print(f"iteration {i}: l is {left} and r is {right}")
            i += 1

            if s[right] != s[left]:
                
                # print("no match")

                if wildcards == 0:
                    
                    # print("no wildcard")

                    # no more wildcards
                    # update left pointer
                    while left == 0 or s[left] == s[left - 1]:
                        left += 1
                    # reset right pointer
                    right = left
                    # reset the number of wildcards left
                    wildcards = k
                else:

                    # print(f"used a wildcard, {wildcards} left")
                    # use a wildcard to convert char at right 
                    # to same as char at left
                    wildcards -= 1

            # update max length of substring
            ans = max(ans, right - left + 1)

            # print(f"the ans after this iteration is {ans}")

            right += 1
        return ans