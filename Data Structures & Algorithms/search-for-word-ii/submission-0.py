class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['eow'] = True
        
        print(trie)
       
        n = len(board)
        m = len(board[0])

        ans = set()

        def traverse(r, c, visited, path, t):
            if (r, c) in visited:
                return

            # found a word
            if 'eow' in t:
                ans.add(path)

            # out of bound
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            cha = board[r][c]

            visited.add((r,c))

            if cha in t:
                traverse(r-1, c, visited, path+cha, t[cha])
                traverse(r+1, c, visited, path+cha, t[cha])
                traverse(r, c-1, visited, path+cha, t[cha])
                traverse(r, c+1, visited, path+cha, t[cha])
            
            visited.remove((r,c))
        
        for r in range(n):
            for c in range(m):
                traverse(r, c, set(), "", trie)
        
        return list(ans)
