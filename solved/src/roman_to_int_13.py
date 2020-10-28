class Solution:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def symbol_smaller_than_next(self, s: str, pos: int) -> bool:
        """
        return if s[pos] is a smaller symbol than s[pos+1]
        """
        if pos == len(s) - 1:
            # is the last symbol in string
            return False
        idx1 = list(self.symbols.keys()).index(s[pos])
        idx2 = list(self.symbols.keys()).index(s[pos + 1])

        return idx1 < idx2

    def romanToInt(self, s: str) -> int:
        result = 0
        for start in range(len(s)):
            symbol = s[start]
            if self.symbol_smaller_than_next(s, start):
                result -= self.symbols[symbol]
            else:
                result += self.symbols[symbol]

        return result



