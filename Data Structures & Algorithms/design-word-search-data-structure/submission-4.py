class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = dict()
            d = d[c]
        d['eow'] = True

    def search(self, word: str) -> bool:
        def traverse(i, d):
            if i == len(word):
                if 'eow' in d:
                    return True
                return False
            
            c = word[i]
            
            if c == '.':
                if len(d) == 0:
                    return False
                ans = False
                for wildcard in d:
                    if wildcard != 'eow':
                        ans = ans or traverse(i+1, d[wildcard])
                return ans
            else:
                if c not in d:
                    return False
                return traverse(i+1, d[c])
            
        return traverse(0, self.trie)


        
