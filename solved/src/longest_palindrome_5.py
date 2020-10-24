class Solution:
    def odd_palindrome_centered_at(self, s: str, pos: int) -> str:
        """
        center at pos, palindrome needs to be odd length
        """
        left_length = pos
        right_length = len(s) - pos - 1

        search_length = min(left_length, right_length)
        for i in range(1, search_length + 1):
            if s[pos - i] == s[pos + i]:
                continue
            else:
                return s[pos - i + 1:pos + i]

        return s[pos - search_length:pos + search_length + 1]

    def even_palindrome_centered_at(self, s: str, pos: int) -> str:
        """
        center at pos and pos+1, palindrome needs to be even length
        :param s:
        :param pos:
        :return:
        """
        if s[pos] != s[pos + 1]:
            return ""

        left_length = pos
        right_length = len(s) - pos - 2

        search_length = min(left_length, right_length)
        for i in range(1, search_length + 1):
            if s[pos - i] == s[pos + i + 1]:
                continue
            else:
                return s[pos - i + 1:pos + i + 1]

        return s[pos - search_length:pos + search_length + 2]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            temp_odd_palindrome = self.odd_palindrome_centered_at(s, i)
            if len(temp_odd_palindrome) > len(longest):
                longest = temp_odd_palindrome

        if len(s) >= 2:
            for i in range(len(s) - 1):
                temp_even_palindrom = self.even_palindrome_centered_at(s, i)
                if len(temp_even_palindrom) > len(longest):
                    longest = temp_even_palindrom

        return longest