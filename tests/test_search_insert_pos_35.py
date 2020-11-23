from search_insert_pos_35 import Solution


def test_with_ex1():
    nums = [1, 3, 5, 6]
    target = 5
    r = Solution().searchInsert(nums, target)
    assert r == 2


def test_with_ex2():
    nums = [1, 3, 5, 6]
    target = 2
    r = Solution().searchInsert(nums, target)
    assert r == 1


def test_with_ex3():
    nums = [1, 3, 5, 6]
    target = 7
    r = Solution().searchInsert(nums, target)
    assert r == 4


def test_with_ex4():
    nums = [1, 3, 5, 6]
    target = 0
    r = Solution().searchInsert(nums, target)
    assert r == 0


def test_with_ex5():
    nums = [1]
    target = 0
    r = Solution().searchInsert(nums, target)
    assert r == 0
