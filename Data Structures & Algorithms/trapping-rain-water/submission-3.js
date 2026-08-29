class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        // to look for greater number we have to keep expanding
        // from an index as long as its left and right neighbour
        // are increasing
        let s_max = [...height];
        let p_max = [...height];
        let len = height.length;

        for (let i = 1; i < len; i++) {
            s_max[i] = Math.max(height[i], s_max[i - 1]);
            let j = len - 1 - i;
            p_max[j] = Math.max(height[j], p_max[j + 1]);
        }

        let t_wather = 0;
        height.forEach((h, i) => (t_wather += Math.min(s_max[i], p_max[i]) - h));
        return t_wather;
    }
}
