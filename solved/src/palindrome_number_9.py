class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_list = list(reversed(list(str(x))))

        return str(x) == ''.join(reversed_list)


