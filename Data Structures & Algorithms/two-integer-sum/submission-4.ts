class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {

        let seenMap = new Map()

        for (let i=0; i < nums.length; i++){

            let num = nums[i]
            if (seenMap.has(num)) return [seenMap.get(num), i]
            else seenMap.set(target-num, i)

        }

    }
}
