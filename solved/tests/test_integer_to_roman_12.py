from integer_to_roman_12 import Solution


def test_get_roman_for_digit_3():
    r = Solution().get_roman_for_digit(3, 1)
    assert r == 'III'


def test_get_roman_for_digit_70():
    r = Solution().get_roman_for_digit(7, 10)
    assert r == 'LXX'


def test_get_roman_for_digit_400():
    r = Solution().get_roman_for_digit(4, 100)
    assert r == 'CD'


def test_get_roman_for_digit_2000():
    r = Solution().get_roman_for_digit(2, 1000)
    assert r == 'MM'

def test_intToRoman_ex1():
    r = Solution().intToRoman(3)
    assert r == "III"
def test_intToRoman_ex2():
    r = Solution().intToRoman(4)
    assert r == "IV"
def test_intToRoman_ex3():
    r = Solution().intToRoman(9)
    assert r == "IX"
def test_intToRoman_ex4():
    r = Solution().intToRoman(58)
    assert r == "LVIII"
def test_intToRoman_ex5():
    r = Solution().intToRoman(1994)
    assert r == "MCMXCIV"
