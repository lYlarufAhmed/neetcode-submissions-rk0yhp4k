class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let calculated = new Map([
            [1, 1],
            [2, 2],
            [3, 3],
        ]);
        const helper = (left) => {
            if (!calculated.has(left)) calculated.set(left, helper(left - 1) + helper(left - 2));
            return calculated.get(left);
        };

        return helper(n);
        // console.log(calculated);
        // return calculated.get(n);
    }
}
