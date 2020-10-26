from container_with_most_water_11 import Solution


def test_findArea():
    height = [3, 4]
    r = Solution().findArea(height, 0, 1)
    assert r == 3


def test_find_bigger_container_false():
    height = [3, 4]
    r = Solution().find_bigger_container(height, 3, 0, 1)
    assert r == 0


def test_find_bigger_container_true():
    height = [3, 4]
    r = Solution().find_bigger_container(height, 2, 0, 1)
    assert r == 3


def test_max_area_ex1():
    height = [1,8,6,2,5,4,8,3,7]
    r = Solution().maxArea(height)
    assert r == 49


def test_max_area_ex2():
    height = [1, 1]
    r = Solution().maxArea(height)
    assert r == 1


def test_max_area_ex3():
    height = [4, 3, 2, 1, 4]
    r = Solution().maxArea(height)
    assert r == 16


def test_max_area_ex4():
    height = [1, 2, 1]
    r = Solution().maxArea(height)
    assert r == 2
