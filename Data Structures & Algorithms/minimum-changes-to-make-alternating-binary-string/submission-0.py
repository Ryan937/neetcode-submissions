class Solution:
    def minOperations(self, s: str) -> int:
        start_with_zero = 0
        start_with_one = 0

        for i, ch in enumerate(s):
            expected_zero = '0' if i % 2 == 0 else '1'
            expected_one = '1' if i % 2 == 0 else '0'

            if ch != expected_zero:
                start_with_zero += 1
            if ch != expected_one:
                start_with_one += 1

        return min(start_with_zero, start_with_one)