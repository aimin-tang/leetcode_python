from letter_combinations_of_a_phone_number_17 import Solution


def test_digit_to_letters():
    r = Solution().digit_to_letters('3')
    assert r == ['d', 'e', 'f']


def test_letterCombinations_ex1():
    r = Solution().letterCombinations('23')
    assert set(r) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


def test_letterCombinations_ex2():
    r = Solution().letterCombinations('')
    assert set(r) == set([])


def test_letterCombinations_ex3():
    r = Solution().letterCombinations('2')
    assert set(r) == set(["a", "b", "c"])
