class Solution:
    def get_roman_for_digit(self, d: int, digit_position: int) -> str:
        """

        :param d: 0-9. single digit number
        :param digit_position: 1, 10, 100, or 1000. 1: 1's position, 10: 10's position, etc.
        :return:
        """
        building_blocks_dict = {
            1: ['I', 'V', 'X'],
            10: ['X', 'L', 'C'],
            100: ['C', 'D', 'M'],
            1000: ['M', '', ''],
        }

        building_blocks = building_blocks_dict[digit_position]

        d_dict = {
            0: '',
            1: building_blocks[0],
            2: building_blocks[0] * 2,
            3: building_blocks[0] * 3,
            4: building_blocks[0] + building_blocks[1],
            5: building_blocks[1],
            6: building_blocks[1] + building_blocks[0],
            7: building_blocks[1] + building_blocks[0] * 2,
            8: building_blocks[1] + building_blocks[0] * 3,
            9: building_blocks[0] + building_blocks[2]
        }
        return d_dict[d]

    def intToRoman(self, num: int) -> str:
        digits = [int(d) for d in list(f'{num:04d}')]
        positions = [1000, 100, 10, 1]
        result = ""
        for digit, position in zip(digits, positions):
            result += self.get_roman_for_digit(digit, position)

        return result

