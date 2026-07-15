class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for curr in strs[1:]:
            j = 0

            while j < len(result) and j < len(curr):
                if result[j] != curr[j]:
                    break
                j += 1

            result = result[:j]

            if result == "":
                return ""

        return result