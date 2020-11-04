from remove_nth_19 import Solution, ListNode


def test_find_length():
    node4 = ListNode(5)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node0 = ListNode(1, node1)

    r = Solution().find_length(node0)
    assert r == 5


def test_get_nth():
    node4 = ListNode(5)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node0 = ListNode(1, node1)

    r = Solution().get_nth(node0, 5, 0)
    assert r == node0
    r = Solution().get_nth(node0, 5, 2)
    assert r == node2

def test_remove_ex1():
    node4 = ListNode(5)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node0 = ListNode(1, node1)

    Solution().removeNthFromEnd(node0, 2)
    r = Solution().get_nth(node0, 4, 3)
    assert r == node4

def test_remove_ex2():
    node0 = ListNode(1)

    r = Solution().removeNthFromEnd(node0, 1)
    assert r == None

def test_remove_ex3():
    node1 = ListNode(2)
    node0 = ListNode(1, node1)

    Solution().removeNthFromEnd(node0, 1)
    r = Solution().get_nth(node0, 1, 0)
    assert r.val == 1
    assert r.next == None
