class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        se = set()
        max_len = 0
        for r in range(len(s)):
            while(s[r] in se):
                se.remove(s[l])
                l += 1
            se.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len