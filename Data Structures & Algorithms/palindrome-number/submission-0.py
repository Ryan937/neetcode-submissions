class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        string = ""

        while x > 0:
            string += str(x % 10)
            x //= 10

        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False

            i += 1
            j -= 1

        return True