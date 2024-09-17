class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        arr = []
        for r in range(0, len(s)):
            while s[r] in arr:
                arr.pop(0)
                l += 1
            arr.append(s[r])
            max_len = max(max_len, len(arr))
        return max_len