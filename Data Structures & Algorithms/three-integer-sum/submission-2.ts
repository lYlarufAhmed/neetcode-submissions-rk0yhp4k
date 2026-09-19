class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        let res: Set<String> = new Set();
        for (let ind = 0; ind < nums.length - 1; ind++) {
            let item = nums[ind];
            let comp_item = 0 - item;
            let lookupM = new Set();
            for (let indI = ind + 1; indI < nums.length; indI++) {
                let itemI = nums[indI];
                let comp_itemI = comp_item - itemI;
                if (lookupM.has(itemI)) {
                    res.add([item, comp_itemI, itemI].sort().join(","));
                } else {
                    lookupM.add(comp_itemI);
                }
            }
        }
        return Array.from(res.values()).map((str) => str.split(",").map((c) => Number(c)));
    }
}
