class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        len_height = len(height)
        for i, i_w in enumerate(height):

            leftMax = i_w
            rightMax = i_w
            for j in range(i-1, -1, -1):
                leftMax = max(height[j], leftMax)
            for k in range(i+1, len_height):
                rightMax = max(height[k], rightMax)
            # print(i, i_w, leftMax, rightMax)
            water += min(leftMax, rightMax) - i_w 
        return water

        