class Solution:
    def needle_at_position(self, haystack: str, needle: str, pos: int) -> int:
        if len(needle) + pos > len(haystack):
            return -1
        if haystack[pos:pos+len(needle)] == needle:
            return pos
        else:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            tmp_result = self.needle_at_position(haystack, needle, i)
            if tmp_result != -1:
                return tmp_result

        return -1


