class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost: number[]): number {
        let mem = new Map();
        let calculateCost = (index: number): number => {
            if (index >= cost.length) return 0;
            let i_1 = mem.get(index + 1) || calculateCost(index + 1);
            mem.set(index + 1, i_1);
            let i_2 = mem.get(index + 2) || calculateCost(index + 2);
            mem.set(index + 2, i_2);

            let cost_i = cost[index] + Math.min(i_1, i_2);
            mem.set(index, cost_i);
            return cost_i;
        };

        return Math.min(calculateCost(0), calculateCost(1));
    }
}
