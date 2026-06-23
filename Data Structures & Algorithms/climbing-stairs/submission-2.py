class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        two_before = 1
        one_before = 1

        for i in range(2, n):
            temp = one_before + two_before
            two_before = one_before
            one_before = temp

        return one_before + two_before