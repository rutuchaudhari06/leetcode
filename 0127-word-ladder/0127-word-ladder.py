from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        wset = set(wordList)

        if endWord not in wset:
            return 0

        q = deque([(beginWord, 1)])

        while q:

            word, steps = q.popleft()

            if word == endWord:
                return steps

            lst = list(word)

            for i in range(len(lst)):
                original = lst[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    lst[i] = c
                    new_word = "".join(lst)

                    if new_word in wset:
                        q.append((new_word, steps + 1))
                        wset.remove(new_word)

                lst[i] = original

        return 0