class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dicts = {}
        for x in nums:
            count_dicts[x] = 1 + count_dicts.get(x, 0)
            if(count_dicts[x] == 2):
                return True
        return False