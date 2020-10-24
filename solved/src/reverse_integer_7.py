class Solution:
    def is_out_of_range(self, x):
        return x < (2 ** 31) * (-1) or x > (2 ** 31 - 1)

    def reverse(self, x: int) -> int:
        # if out of range
        if self.is_out_of_range(x):
            return 0

        # if 0
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1

        # if negative
        if x < 0:
            x = x * -1

        xs = str(x)
        xs_reversed = ''.join(reversed(xs))

        result = sign * int(xs_reversed)
        if self.is_out_of_range(result):
            return 0

        return result
