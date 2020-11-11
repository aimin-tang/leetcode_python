from strstr_28 import Solution


def test_needle_at_position():
    s = 'abcde'
    r = Solution().needle_at_position(s, 'de', 3)
    assert r == 3
    r = Solution().needle_at_position(s, 'de', 4)
    assert r == -1
    r = Solution().needle_at_position(s, 'be', 1)
    assert r == -1


def test_strStr_ex1():
    haystack = "hello"
    needle = "ll"
    r = Solution().strStr(haystack, needle)
    assert r == 2


def test_strStr_ex2():
    haystack = "aaaaa"
    needle = "bba"
    r = Solution().strStr(haystack, needle)
    assert r == -1


def test_strStr_ex3():
    haystack = ""
    needle = ""
    r = Solution().strStr(haystack, needle)
    assert r == 0
