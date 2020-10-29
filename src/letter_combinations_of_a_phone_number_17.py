from typing import List
from itertools import chain


class Solution:
    def digit_to_letters(self, digit: str) -> List[str]:
        d2l = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        return d2l[digit]

    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        for digit in digits:
            letters = self.digit_to_letters(digit)
            tmp_list = []
            if result:    # not empty
                for letter in letters:
                    tmp_list.append([w+letter for w in result])
            else:         # empty result
                tmp_list = letters

            result = list(chain.from_iterable(tmp_list))

        return result
