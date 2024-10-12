class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def cmp(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        nums = [bin(i)[2:] for i in nums]
        nums.sort(key=cmp_to_key(cmp))
        return int(''.join(nums), 2)