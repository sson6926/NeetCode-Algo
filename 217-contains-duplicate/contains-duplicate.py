class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dicts = {}
        for x in nums:
            if(count_dicts.get(x) == None):
                count_dicts[x] = 1
            else:
                return True
        return False