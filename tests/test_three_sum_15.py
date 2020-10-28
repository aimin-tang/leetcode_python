from three_sum_15 import Solution


def test_find_the_other_two():
    nums = [-5, -2, -1, 6, 7]
    r = Solution().find_the_other_two(nums, 0)
    assert r == [(-5, -2, 7), (-5, -1, 6)]

def test_threeSum_ex1():
    nums = [-1,0,1,2,-1,-4]
    r = Solution().threeSum(nums)
    r.sort()
    assert r == [[-1,-1,2],[-1,0,1]]

def test_threeSum_ex2():
    nums = []
    r = Solution().threeSum(nums)
    assert r == []

def test_threeSum_ex3():
    nums = [0]
    r = Solution().threeSum(nums)
    assert r == []


def test_threeSum_ex4():
    nums = [0, 0, 0]
    r = Solution().threeSum(nums)
    assert r == [[0, 0, 0]]
