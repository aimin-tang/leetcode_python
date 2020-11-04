class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_length(self, head: ListNode) -> int:
        result = 1
        temp_node = head

        while temp_node.next:
            temp_node = temp_node.next
            result += 1

        return result

    def get_nth(self, head: ListNode, l: int, n: int) -> ListNode:
        if n == 0:
            return head

        curr_idx = 1
        curr_node = head.next

        for pos in range(1, l):
            if curr_idx == n:
                return curr_node
            else:
                curr_idx += 1
                curr_node = curr_node.next
        else:
            raise ValueError("invalid n for get_nth: {}".format(n))

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = self.find_length(head)
        if n > l or n < 1:
            raise ValueError("invalid value for {}".format(n))

        if n == 1 and l == 1:
            return None

        if n == l:
            result = head.next
            del head
            return result

        if n == 1:
            prev = self.get_nth(head, l, l - 2)
            last_node = prev.next
            prev.next = None
            del last_node
            return head

        prev = self.get_nth(head, l, l - n - 1)
        tempNode = prev.next
        prev.next = tempNode.next
        del tempNode
        return head

