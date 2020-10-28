from longest_common_prefix_14 import Solution


def test_with_ex1():
    strs = ["flower", "flow", "flight"]
    r = Solution().longestCommonPrefix(strs)
    assert r == 'fl'

def test_with_ex2():
    strs = ["dog","racecar","car"]
    r = Solution().longestCommonPrefix(strs)
    assert r == ''

def test_with_ex3():
    strs = ["a"]
    r = Solution().longestCommonPrefix(strs)
    assert r == 'a'

