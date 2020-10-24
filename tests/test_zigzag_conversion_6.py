from zigzag_conversion_6 import Solution


def test_get_current_pos_after_i_units():
    s = "PAYPALISHIRING"
    r = Solution().get_current_pos_after_i_units(3, 0)
    assert r == 0
    r = Solution().get_current_pos_after_i_units(3, 2)
    assert r == 8


def test_remaining_chars_in_row():
    s = "PAYPALISHIRING"
    r = Solution().remaining_chars_in_row(s, 3, 0)
    assert r == 3
    r = Solution().remaining_chars_in_row(s, 3, 3)
    assert r == 2


def test_remaining_chars_in_diag():
    s = "PAYPALISHIRINGG"
    r = Solution().remaining_chars_in_diag(s, 3, 0)
    assert r == 1
    r = Solution().remaining_chars_in_diag(s, 3, 3)
    assert r == 0


def test_append_after_i_units():
    s = "PAYPALISHIRING"
    result = []
    Solution().append_after_i_units(result, s, 3, 0)
    assert result == [['P', 'A', 'Y'], [' ', 'P', ' ']]


def test_before_transpose():
    s = "PAYPALISHIRING"
    r = Solution().before_transpose(s, 3)
    assert r == [['P', 'A', 'Y'], [' ', 'P', ' '], ['A', 'L', 'I'], [' ', 'S', ' '],
                 ['H', 'I', 'R'], [' ', 'I', ' '], ['N', 'G', ' ']]


def test_convert():
    s = "PAYPALISHIRING"
    r = Solution().convert(s, 3)
    assert r == "PAHNAPLSIIGYIR"
    r = Solution().convert(s, 4)
    assert r == "PINALSIGYAHRPI"


def test_convert_A():
    s = "A"
    r = Solution().convert(s, 1)
    assert r == "A"
