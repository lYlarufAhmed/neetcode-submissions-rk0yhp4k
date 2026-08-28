class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;

        let water = 0;
        while (left < right) {
            water = Math.max(Math.min(heights[left], heights[right]) * (right - left), water);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return water;
    }
}
