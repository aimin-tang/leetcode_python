from four_sum_18 import Solution


def test_with_ex1():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    r = Solution().fourSum(nums, target)
    assert r == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

def test_with_ex2():
    nums = []
    target = 0
    r = Solution().fourSum(nums, target)
    assert r == []

def test_with_ex3():
    nums = [-2,-1,-1,1,1,2,2]
    target = 0
    r = Solution().fourSum(nums, target)
    assert r == [[-2,-1,1,2],[-1,-1,1,1]]
