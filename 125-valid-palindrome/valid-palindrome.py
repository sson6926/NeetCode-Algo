class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join([x.lower() for x in s if x.isalnum()])
        return ss == ss[::-1]