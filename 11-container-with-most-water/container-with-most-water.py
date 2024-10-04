class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while(l < r):
            res = max(res, (r-l)*min(height[r], height[l]))
            if(height[l] < height[r]):
                l += 1
            elif(height[l] > height[r]):
                r -= 1
            else:
                r -=1
                l += 1
        return res