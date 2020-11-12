class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # get the sign
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        elif divisor == 0:
            raise ValueError("divisor should not be 0")
        else:   # dividend is 0
            return 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        curr_divident = dividend

        while curr_divident >= divisor:
            curr_divident -= divisor
            result += 1

        return result * sign
