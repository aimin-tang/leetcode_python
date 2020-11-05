class Solution:
    def safe_to_remove(self, s: str, pos: int) -> bool:
        """
        if s[pos] and s[pos+1] is matching parens, return true.
        """
        if pos == len(s) - 1:
            return False

        if s[pos] == '(' and s[pos+1] == ')' or \
            s[pos] == '[' and s[pos + 1] == ']' or \
            s[pos] == '{' and s[pos + 1] == '}':
            return True

        return False

    def remove_two_chars(self, s: str, pos: int) -> str:
        """
        remove s[pos] and s[pos+1] from string
        """
        if pos == 0:
            return s[2:]
        else:
            return s[:pos] + s[pos+2:]

    def isValid(self, s: str) -> bool:
        s2 = ''.join([l for l in s])  # s isn't changed by this function
        made_progress = True

        while made_progress:
            made_progress = False
            for pos in range(len(s2)):
                if self.safe_to_remove(s2, pos):
                    s2 = self.remove_two_chars(s2, pos)
                    made_progress = True
                    break

        if len(s2) == 0:
            return True
        else:
            return False



