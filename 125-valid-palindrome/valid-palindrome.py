class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s_mod = [x.lower() for x in s if x.isalnum()]
        r = len(s_mod) -1
        while (l < r):
            if (s_mod[l] != s_mod[r]):
                return False
            l += 1
            r -= 1
        return True