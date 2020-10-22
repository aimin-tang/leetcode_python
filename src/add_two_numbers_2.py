class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val=0, next=None):
        new_node = ListNode(val, next)
        self.next = new_node
        return new_node

    def listify(self):
        result = [self.val]
        next = self.next

        while next:
            result.append(next.val)
            next = next.next

        return result



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_result_and_carry(n1: int, n2: int, carry:int =0) -> tuple[int, int]:
            r = n1 + n2 + carry
            if r < 10:
                return (r, 0)
            else:
                return (r-10, 1)

        val, carry = get_result_and_carry(l1.val, l2.val, 0)
        result_node = ListNode(val)
        curr_l1 = l1
        curr_l2 = l2
        curr_node = result_node
        empty_node = ListNode()

        while True:
            if curr_l1.next or curr_l2.next or carry:
                l1n = curr_l1.next.val if curr_l1.next else 0
                l2n = curr_l2.next.val if curr_l2.next else 0
                val, carry = get_result_and_carry(l1n, l2n, carry)
                new_node = ListNode(val)
                curr_node.next = new_node
                curr_node = new_node
                curr_l1 = curr_l1.next if curr_l1.next else empty_node
                curr_l2 = curr_l2.next if curr_l2.next else empty_node
            else:
                break

        return result_node
