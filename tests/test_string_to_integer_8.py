from string_to_integer_8 import Solution


def test_with_ex1():
    r = Solution().myAtoi("42")
    assert r == 42

def test_with_ex2():
    r = Solution().myAtoi("   -42")
    assert r == -42

def test_with_ex3():
    r = Solution().myAtoi("4193 with words")
    assert r == 4193

def test_with_ex4():
    r = Solution().myAtoi("words and 42")
    assert r == 0

def test_with_ex5():
    r = Solution().myAtoi("   -91283472332")
    assert r == -2147483648

def test_with_ex6():
    r = Solution().myAtoi("3.14")
    assert r == 3

def test_with_ex7():
    r = Solution().myAtoi("  -0012a42")
    assert r == -12
