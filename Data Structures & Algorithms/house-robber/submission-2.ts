class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        let mem = new Map();

        const dfs = (n: number) => {
            if (n >= nums.length) return 0;

            let n_2 = mem.get(n + 2) || dfs(n + 2);
            mem.set(n + 2, n_2);
            let n_1 = mem.get(n + 1) || dfs(n + 1);
            mem.set(n + 1, n_1);

            let n_ = mem.get(n) || Math.max(nums[n] + n_2, n_1);
            mem.set(n, n_);
            return mem.get(n);
        };

        dfs(0);
        return mem.get(0);
    }
}
