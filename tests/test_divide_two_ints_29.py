from divide_two_ints_29 import Solution


def test_with_ex1():
    r = Solution().divide(10, 3)
    assert r == 3
    r = Solution().divide(7, -3)
    assert r == -2
    r = Solution().divide(0, 1)
    assert r == 0
    r = Solution().divide(1, 1)
    assert r == 1
