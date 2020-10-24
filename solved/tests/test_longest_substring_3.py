from longest_substring_3 import Solution


def test_longest_substring():
    s = "aab"
    r = Solution().longestFrom(s, 0)
    assert r == 1
    r = Solution().longestFrom(s, 1)
    assert r == 2


def test_longest_substring_ex1():
    s = "abcabcbb"
    r = Solution().longestFrom(s, 0)
    assert r == 3


def test_with_ex1():
    s = "abcabcbb"
    r = Solution().lengthOfLongestSubstring(s)
    assert r == 3


def test_with_ex2():
    s = "bbbbb"
    r = Solution().lengthOfLongestSubstring(s)
    assert r == 1


def test_with_ex3():
    s = ""
    r = Solution().lengthOfLongestSubstring(s)
    assert r == 0
