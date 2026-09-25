class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let L = 0,
            R = 0,
            max = nums[0],
            maxI = 0,
            res = [];

        while (R - L + 1 < k) {
            R++;
            if (nums[maxI] < nums[R]) {
                max = nums[R];
                maxI = R;
            }
        }
        res.push(max)
        while (R < nums.length-1) {
            if (L == maxI) {
                let j = L + 1;
                maxI = L+1
                max = nums[L+1]
                while (j <= R) {
                    if (nums[j] > max) {
                        max = nums[j];
                        maxI = j;
                    }

                    j++;
                }
            }

            L++;

            if (max < nums[R + 1]) {
                maxI = R + 1;
                max = nums[R + 1];
            }

            R++;

            res.push(max);
        }

        return res;
    }
}
