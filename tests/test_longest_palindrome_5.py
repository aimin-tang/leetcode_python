from longest_palindrome_5 import Solution


def test_is_palindrom():
    r = Solution().is_palindrome('')
    assert r == True
    r = Solution().is_palindrome('aba')
    assert r == True
    r = Solution().is_palindrome('abc')
    assert r == False


def test_longest_from():
    r = Solution().longest_from('babad', 0)
    assert r == 'bab'
    r = Solution().longest_from('babad', 1)
    assert r == 'aba'
    r = Solution().longest_from('babad', 2)
    assert r == 'b'


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
