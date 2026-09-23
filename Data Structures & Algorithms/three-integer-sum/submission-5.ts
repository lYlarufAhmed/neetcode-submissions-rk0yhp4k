class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        let res: number[][] = [];
        nums.sort((a,b)=> a-b)

        for (let i = 0; i < nums.length - 1; i++) {
            let num1 = nums[i];
            if (i > 0 && nums[i] == nums[i - 1]) continue; // dups
            let left = i + 1;
            let right = nums.length - 1;

            while (left < right) {
                let tripSum = num1 + nums[left] + nums[right];

                if (tripSum == 0) {
                    res.push([num1, nums[left], nums[right]]);
                    while (left < right && nums[left] === nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] === nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (tripSum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        //idxS.forEach((s) => res.push(s.split(",").map((n) => Number(n))));
        return res;
    }
}
