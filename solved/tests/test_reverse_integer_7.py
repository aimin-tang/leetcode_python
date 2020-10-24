from reverse_integer_7 import Solution


def test_with_ex1():
    r = Solution().reverse(123)
    assert r == 321


def test_with_ex2():
    r = Solution().reverse(-123)
    assert r == -321


def test_with_ex3():
    r = Solution().reverse(120)
    assert r == 21


def test_with_ex4():
    r = Solution().reverse(0)
    assert r == 0


def test_with_ex5():
    r = Solution().reverse(1534236469)
    assert r == 0
