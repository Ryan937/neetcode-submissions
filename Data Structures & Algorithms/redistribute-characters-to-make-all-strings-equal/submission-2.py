class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = [0] * 26

        for word in words:
            for c in word:
                d[ord(c) - ord('a')] += 1

        n = len(words)

        for i in d:
            if i % n != 0:
                return False

        return True