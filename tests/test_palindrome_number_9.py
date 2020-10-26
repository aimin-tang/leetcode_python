from palindrome_number_9 import Solution


def test_with_ex1():
    r = Solution().isPalindrome(121)
    assert r == True

def test_with_ex2():
    r = Solution().isPalindrome(-121)
    assert r == False

def test_with_ex3():
    r = Solution().isPalindrome(10)
    assert r == False

