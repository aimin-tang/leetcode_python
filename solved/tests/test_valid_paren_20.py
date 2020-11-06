from valid_paren_20 import Solution


def test_safe_to_remove():
    s = "()[]{}"
    r = Solution().safe_to_remove(s, 0)
    assert r == True
    r = Solution().safe_to_remove(s, 1)
    assert r == False


def test_remove_two_chars():
    s = "()[]{}"
    r = Solution().remove_two_chars(s, 0)
    assert r == '[]{}'
    r = Solution().remove_two_chars(s, 4)
    assert r == '()[]'


def test_is_valid_ex1():
    s = "()"
    r = Solution().isValid(s)
    assert r == True


def test_is_valid_ex2():
    s = "()[]{}"
    r = Solution().isValid(s)
    assert r == True


def test_is_valid_ex3():
    s = "(]"
    r = Solution().isValid(s)
    assert r == False


def test_is_valid_ex4():
    s = "([)]{}"
    r = Solution().isValid(s)
    assert r == False


def test_is_valid_ex5():
    s = "([])"
    r = Solution().isValid(s)
    assert r == True
