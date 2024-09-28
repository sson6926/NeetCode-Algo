class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_len = len(nums)
        res = []
        for i in range(num_len):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            else:
                l, r = i+1, num_len-1
                while(l < r):
                    if nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        res.append([nums[i], nums[r], nums[l]])
                        l += 1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
        return res