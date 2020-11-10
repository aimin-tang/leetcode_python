from remove_dup_26 import Solution


def test_with_ex1():
    nums = [1,1,2]
    l = Solution().removeDuplicates(nums)
    assert l == 2
    assert nums == [1, 2]

def test_with_ex2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    l = Solution().removeDuplicates(nums)
    assert l == 5
    assert nums == [0,1,2,3,4]
