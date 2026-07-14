class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        x2 = x

        while x2 > 0:
            curr = x2 % 10
            x2 //= 10

            reversed *= 10
            reversed += curr

        return x == reversed