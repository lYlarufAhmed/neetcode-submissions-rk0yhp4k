class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     * We can use a hashmap to store the previous seen items with
     * index.
     * for each item we look for +/- 1 item. when found we can store the
     * last seen item
     *
     * we have to store both index and the count including the num
     * itself.
     * start 0 - 2
     * longest 2
     *
     * i start  len longest
     * 0    0   1   -inf
     * 1    0   2   -inf
     * 2    2   1   i - start = 2
     * 3    2   2   2
     * 4    4
     * 5
     * 6
     * 7    2   5
     * 0 1 1 2 3 4 5 6 7
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);
        let res = 0

        let length = 0;

        for (let num of nums) {
            if (!numSet.has(num - 1)) {
                length = 1;
                while (numSet.has(num + length)) {
                    length++;
                }
            }
            res = Math.max(length, res)
        }

        return res
    }
}
// 2, 3, 4, 5, 10, 20
// 0, 1, 1, 2, 3, 4, 5, 6
