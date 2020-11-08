from typing import List


class Solution:
    def ok_at_char(self, one_result: str, pos1: int, pos2: int) -> bool:
        """If we insert '(' before pos1, tell whether ')' can be inserted before
        pos2 to match the '(' at pos1"""
        sub_str = one_result[pos1:pos2]
        if sub_str.count('(') == sub_str.count(')'):
            return True
        else:
            return False


    def generate_from_pos(self, prev_result: List[str], pos: int) -> List[str]:
        "Insert '(' at pos. Return all valid strings after"

        result = []
        for one_result in prev_result:
            for i in range(pos, len(one_result)+1):
                if self.ok_at_char(one_result, pos, i):
                    result.append(one_result[:pos] + '(' + one_result[pos:i] \
                                  + ')' + one_result[i:])
        return result


    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1 or n > 9:
            raise ValueError("1 <= n <= 8, but got {}".format(n))

        if n == 1:
            return ["()"]
        else:
            result = []
            prev_result = self.generateParenthesis(n - 1)
            for i in range(len(prev_result) + 1):
                result.extend(self.generate_from_pos(prev_result, i))

            return sorted(list(set(result)))

