class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let left = 0;
        let right = heights.length - 1;
        let max_total = 0;

        let total = 0;

        while (left < right) {
            //console.log(max_total);
            max_total = Math.max(
                max_total,
                Math.min(heights[left], heights[right]) * (right - left),
            );
            if (heights[right] > heights[left]) {
                left++;
            } else {
                right--;
            }
        }
        return max_total;
    }
}
