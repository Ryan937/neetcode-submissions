class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, result = 0, 0, 0
        dupes = set()

        while j < len(s):
            if s[j] in dupes:
                dupes.remove(s[i])
                i += 1
            else:
                dupes.add(s[j])
                j += 1
                result = max(result, j - i)

        return result