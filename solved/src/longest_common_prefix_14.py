from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            # no strs
            return ''
        if len(strs[0]) == 0:
            # first string is empty
            return ''

        result = ''
        for end in range(0, len(strs[0])):
            prefix = strs[0][:end+1]
            if all([str.startswith(prefix) for str in strs]):
                result = prefix
            else:
                break

        return result
