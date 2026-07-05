class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, depth = q.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i + 1 :]

                    if next_word == endWord:
                        return depth + 1

                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, depth + 1))

        return 0
