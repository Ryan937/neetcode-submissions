class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        result = prices[0] + prices[1]

        return money - result if result <= money else money 