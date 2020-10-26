class Solution:
    def is_digit(self, c: str) -> bool:
        digits = [str(d) for d in range(10)]
        return c in digits

    def handle_leading_sign(self, s: str) -> tuple:
        sign = 1
        if len(s) > 0:
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                sign = 1
                s = s[1:]
        else:
            return 1, ""

        return sign, s

    def handle_trailing_words(self, s:str) -> str:
        for idx, c in enumerate(s):
            if self.is_digit(c) or c == '.':
                continue
            else:
                return s[:idx]

        return s

    def handle_dot(self, s: str) -> str:
        s = s.split('.')
        if len(s) == 0:
            return ""
        else:
            return s[0]

    def handle_out_of_range(self, i: int) -> int:
        if i > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif i < 2 ** 31 * (-1):
            return 2 ** 31 * (-1)
        else:
            return i

    def myAtoi(self, s: str) -> int:
        # handle leading spaces
        s = s.strip()

        # handle leading "+" or "-"
        sign, s = self.handle_leading_sign(s)

        # handle trailing words
        s = self.handle_trailing_words(s)

        # handle "."
        s = self.handle_dot(s)

        # convert it
        result = 0
        for i in range(len(s)):
            result = result * 10 + int(s[i])
        result *= sign

        # handle out of range
        return self.handle_out_of_range(result)
