from roman_to_int_13 import Solution


def test_symbol_smaller_than_next_1():
    r = Solution().symbol_smaller_than_next('IV', 0)
    assert r == True
    r = Solution().symbol_smaller_than_next('VI', 0)
    assert r == False
    r = Solution().symbol_smaller_than_next('VI', 1)
    assert r == False

def test_roman_to_int():
    r = Solution().romanToInt('III')
    assert r == 3
    r = Solution().romanToInt('IV')
    assert r == 4
    r = Solution().romanToInt('IX')
    assert r == 9
    r = Solution().romanToInt('LVIII')
    assert r == 58
    r = Solution().romanToInt('MCMXCIV')
    assert r == 1994
