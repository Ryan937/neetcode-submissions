class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        prev = [1, 1]
        curr = 2

        while curr <= rowIndex:
            result = []

            for i in range(curr + 1):
                if i == 0 or i == curr:
                    result.append(1)
                else:
                    result.append(prev[i - 1] + prev[i])

            curr += 1
            prev = result

        return prev