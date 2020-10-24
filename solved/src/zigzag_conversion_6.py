from itertools import chain

class Solution:
    def get_current_pos_after_i_units(self, numRows: int, i: int) -> int:
        unit_length = 2 * numRows - 2
        curr_pos = i * unit_length

        return curr_pos

    def remaining_chars_in_row(self, s: str, numRows: int, i: int) -> int:
        "Find how many chars we can fill in the row"
        curr_pos = self.get_current_pos_after_i_units(numRows, i)
        remaining_chars = len(s) - curr_pos

        return min(remaining_chars, numRows)

    def remaining_chars_in_diag(self, s: str, numRows: int, i: int) -> int:
        "Find how many single-letter rows in diagonal we need to fill"
        curr_pos = self.get_current_pos_after_i_units(numRows, i) + numRows
        remaining_chars = len(s) - curr_pos

        return min(remaining_chars, numRows - 2)

    def append_after_i_units(self, result: list, s: str,
                             numRows: int, i: int) -> None:
        """append to the result, after the ith full unit. A full unit is a
        full row plus diagonal before next full row"""
        curr_pos = self.get_current_pos_after_i_units(numRows, i)

        chars_in_row = self.remaining_chars_in_row(s, numRows, i)
        if chars_in_row < numRows:
            curr_row = s[curr_pos:]
            missing_spaces = numRows - len(curr_row)
            curr_row += missing_spaces * ' '
            result.append(list(curr_row))
            return

        result.append(list(s[curr_pos:curr_pos + numRows]))

        chars_in_diag = self.remaining_chars_in_diag(s, numRows, i)

        for j in range(chars_in_diag):
            leading_spaces = numRows - j - 2
            trailing_spaces = j + 1
            curr_row = leading_spaces * ' '
            curr_row += s[curr_pos + numRows + j]
            curr_row += trailing_spaces * ' '
            result.append(list(curr_row))

    def before_transpose(self, s: str, numRows: int) -> list:
        unit_length = 2 * numRows - 2

        result = []
        for i in range(len(s) // unit_length + 1):
            self.append_after_i_units(result, s, numRows, i)

        return result

    def convert(self, s: str, numRows: int) -> list:
        if numRows == 1:
            return s

        before_transpose = self.before_transpose(s, numRows)
        transposed = zip(*before_transpose)
        flattened = ''.join(chain(*transposed))
        stripped = flattened.replace(' ', '')

        return stripped
