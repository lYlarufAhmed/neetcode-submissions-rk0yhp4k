class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        let res: number[][] = [];
        let idxS: Set<string> = new Set();

        for (let i = 0; i < nums.length - 1; i++) {
            let num1 = nums[i];
            let t = 0 - num1;
            let seenMap = new Map();
            for (let j = i + 1; j < nums.length; j++) {
                let num2 = nums[j];
                if (seenMap.has(num2)) {
                    idxS.add([nums[i], nums[seenMap.get(num2)], nums[j]].sort().join(","));
                } else seenMap.set(t - num2, j);
            }
        }

        idxS.forEach((s) => res.push(s.split(",").map((n) => Number(n))));
        return res;
    }
}
