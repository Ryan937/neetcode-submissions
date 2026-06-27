class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for num in nums:
            if num not in seen:
                seen.add(num)

        n = len(nums) + 1

        for i in range(1, n):
            if i not in seen:
                result.append(i)

        return result