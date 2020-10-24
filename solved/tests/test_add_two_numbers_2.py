from add_two_numbers_2 import ListNode, Solution


def test_with_ex1():
    node11 = ListNode(2)
    node12 = node11.append(4)
    node12.append(3)

    node21 = ListNode(5)
    node22 = node21.append(6)
    node22.append(4)

    r = Solution().addTwoNumbers(node11, node21).listify()
    assert r == [7, 0, 8]


def test_with_ex2():
    node11 = ListNode(0)
    node21 = ListNode(0)

    r = Solution().addTwoNumbers(node11, node21).listify()
    assert r == [0]


def test_with_ex3():
    node11 = ListNode(9)
    node12 = node11.append(9)
    node13 = node12.append(9)
    node14 = node13.append(9)
    node15 = node14.append(9)
    node16 = node15.append(9)
    node16.append(9)

    node21 = ListNode(9)
    node22 = node21.append(9)
    node23 = node22.append(9)
    node23.append(9)

    r = Solution().addTwoNumbers(node11, node21).listify()
    assert r == [8, 9, 9, 9, 0, 0, 0, 1]
