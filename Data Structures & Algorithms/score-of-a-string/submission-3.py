class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j, n = 0, 1, len(s)
        result = 0

        while j < n:
            result += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1

        return result