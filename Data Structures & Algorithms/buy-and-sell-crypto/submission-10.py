class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, result = 0, 1, 0

        while j < len(prices):
            curr = prices[j] - prices[i]
            result = max(result, curr)

            if curr < 0:
                i += 1
            else:
                j += 1

        return result