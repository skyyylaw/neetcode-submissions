class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = dict()
        for word in strs:
            t = trie
            for cha in word:
                if cha not in t:
                    t[cha] = dict()
                t = t[cha]
            t['eow'] = True
        ans = ""
        t = trie

        while len(t) == 1 and 'eow' not in t:
            print(t)
            cha = list(t.keys())[0]
            ans = ans + cha
            t = t[cha]
           
            
            
        return ans
