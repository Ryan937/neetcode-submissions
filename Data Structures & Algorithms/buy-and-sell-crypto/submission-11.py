class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, result = 0, 1, 0

        while j < len(prices):
            curr = prices[j] - prices[i]

            if curr > 0:
                result = max(result, curr)
            else:
                i = j

            j += 1

        return result