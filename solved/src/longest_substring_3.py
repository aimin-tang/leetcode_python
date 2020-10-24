class Solution:
    def longestFrom(self, s: str, pos: int) -> int:
        if len(s[pos:]) == 0:
            return 0

        longest = 1
        sub_string = s[pos:]
        for i in range(1, len(sub_string)):
            if sub_string[i] in sub_string[:i]:
                if i > longest:
                    longest = i
                break
            if i == len(sub_string) - 1:
                if i + 1 > longest:
                    longest = i + 1
                break

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        all_results = [self.longestFrom(s, i) for i in range(len(s))]
        if len(all_results) == 0:
            return 0
        return max(all_results)
