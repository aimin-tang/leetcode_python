from generate_parentheses_22 import Solution


def test_ok_at_char():
    one_result = '()'
    r = Solution().ok_at_char(one_result, 0, 0)
    assert r == True
    r = Solution().ok_at_char(one_result, 0, 1)
    assert r == False
    r = Solution().ok_at_char(one_result, 0, 2)
    assert r == True
    r = Solution().ok_at_char(one_result, 1, 1)
    assert r == True
    r = Solution().ok_at_char(one_result, 1, 2)
    assert r == False
    r = Solution().ok_at_char(one_result, 2, 2)
    assert r == True

def test_generate_from_pos():
    prev_result = ['()']
    r = Solution().generate_from_pos(prev_result, 0)
    assert r == ['()()', '(())']

def test_generateParenthesis():
    r = Solution().generateParenthesis(1)
    assert r == ['()']
    r = Solution().generateParenthesis(2)
    assert r == sorted(['()()', '(())'])
    r = Solution().generateParenthesis(3)
    assert r == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
