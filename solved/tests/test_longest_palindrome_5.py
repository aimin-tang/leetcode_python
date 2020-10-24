from longest_palindrome_5 import Solution


def test_odd_palindrome_centered_at_case1():
    r = Solution().odd_palindrome_centered_at('abcbe', 2)
    assert r == 'bcb'


def test_odd_palindrome_centered_at_case2():
    r = Solution().odd_palindrome_centered_at('abcbe', 1)
    assert r == 'b'


def test_even_palindrome_centered_at_case2():
    r = Solution().even_palindrome_centered_at('bb', 0)
    assert r == 'bb'


def test_with_ex1():
    r = Solution().longestPalindrome('babad')
    assert r in ['bab', 'aba']


def test_with_ex2():
    r = Solution().longestPalindrome('cbbd')
    assert r == 'bb'


def test_with_ex3():
    r = Solution().longestPalindrome('a')
    assert r == 'a'


def test_with_ex4():
    r = Solution().longestPalindrome('ac')
    assert r in ['a', 'c']

def test_with_bb():
    r = Solution().longestPalindrome('bb')
    assert r == 'bb'
