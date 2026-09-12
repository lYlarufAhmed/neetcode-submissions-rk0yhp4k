class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost: number[]): number {
        let prev1 = cost[0];
        let prev2 = cost[1];
        let current;

        let start = 2;

        while (start < cost.length) {
            current = cost[start] + Math.min(prev1, prev2);

            prev1 = prev2;
            prev2 = current;
            start++;
        }

        console.log(prev1, prev2);

        return Math.min(prev1, prev2);
    }
}
