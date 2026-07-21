class PrefixTree:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        d = self.trie
        for i, c in enumerate(word):
            if c not in d:
                d[c] = dict()
            d = d[c]
        d['EOW'] = True


    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return 'EOW' in d
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
        