from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    nxt = word[:i] + c + word[i + 1:]

                    if nxt in words:
                        words.remove(nxt)
                        q.append((nxt, dist + 1))

        return 0