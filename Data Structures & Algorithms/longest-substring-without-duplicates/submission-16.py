class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, result = 0, 0, 0
        dupes = set()

        while j < len(s):
            if s[j] not in dupes:
                dupes.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                dupes.remove(s[i])
                i += 1
        
        return result