class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let seenMap = new Map();

        for (let i = 0; i < numbers.length; i++) {
            let curr = numbers[i];
            if (seenMap.has(curr)) return [seenMap.get(curr) + 1, i + 1];
            let comp = target - curr;
            seenMap.set(comp, i);
        }
    }
}
