class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set()

        for c in allowed:
            seen.add(c)

        result = 0

        for word in words:
            for i in range(len(word)):
                if word[i] not in seen:
                    break
                
                if i == len(word) - 1:
                    result += 1

        return result