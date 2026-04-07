class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        l, h = 0, len(height)-1

        while l < h:
            area = min(height[l], height[h]) * (h-l)

            res = max(res, area)

            if height[l] <= height[h]:
                l+=1
            else:
                h-= 1
        return res