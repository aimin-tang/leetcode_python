class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def longest_from(self, s: str, pos: int) -> str:
        # empty should be handled before here
        longest = s[pos]
        sub_string = s[pos:]
        # can improve a lot on speed
        for i in range(len(sub_string), 1, -1):
            if self.is_palindrome(sub_string[:i]):
                if len(sub_string[:i]) > len(longest):
                    longest = sub_string[:i]
                break

        return longest

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        result = []
        for i in range(len(s)):
            result.append(self.longest_from(s, i))
            result.sort(key=lambda x: len(x), reverse=True)

        return result[0]

