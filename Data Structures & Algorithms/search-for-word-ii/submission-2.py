class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["END"] = True
            node["WORD"] = w

        presentWords = set()
        visited = set()

        def findWord(r, c, node):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in visited:
                return
            if board[r][c] not in node:
                return
            
            node = node[board[r][c]]
            if "END" in node:
                presentWords.add(node["WORD"])

            visited.add((r,c))
            for d in (1, -1):
                for nextR, nextC in ((r+d, c), (r, c+d)):
                    findWord(nextR, nextC, node)
            visited.remove((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                findWord(r, c, trie)
        
        return list(presentWords)