from three_sum_closest_16 import Solution


def test_three_sum_closest_on_n1():
    nums = [-4, -1, 1, 2]
    r = Solution().three_sum_closest_on_n1(nums, 0, 1)
    assert r == -1
    r = Solution().three_sum_closest_on_n1(nums, 1, 1)
    assert r == 2


def test_threeSumClosest_ex1():
    nums = [-4, -1, 1, 2]
    r = Solution().threeSumClosest(nums, 1)
    assert r == 2


def test_three_sum_closest_on_n1_ex2():
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    r = Solution().three_sum_closest_on_n1(nums, 1, 82)
    assert r == 82


def test_threeSumClosest_ex2():
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    r = Solution().threeSumClosest(nums, 82)
    assert r == 82

def test_three_sum_closest_on_n1_ex3():
    nums = [-5, -5, -4, 0, 0, 3, 3, 4, 5]
    r = Solution().three_sum_closest_on_n1(nums, 1, -2)
    assert r == -2


def test_threeSumClosest_ex3():
    nums = [4,0,5,-5,3,3,0,-4,-5]
    r = Solution().threeSumClosest(nums, -2)
    assert r == -2
