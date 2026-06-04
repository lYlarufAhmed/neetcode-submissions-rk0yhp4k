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
        if (nums.length == 0) return 0
        let res = 1;
        const sortedNums = nums.sort((a,b)=> a-b);
        console.log(sortedNums)
        let currStreak = 1;
        for (let i = 0; i < nums.length - 1; i++) {
            let curr = sortedNums[i];
            let nextI = sortedNums[i + 1];
            if (curr == nextI) continue;
            else if (nextI - curr > 1) {
                res = Math.max(currStreak, res);
                currStreak = 1;
            } else currStreak++;
        }
        res = Math.max(currStreak, res);
        return res;
    }
}
// 2, 3, 4, 5, 10, 20
// 0, 1, 1, 2, 3, 4, 5, 6
