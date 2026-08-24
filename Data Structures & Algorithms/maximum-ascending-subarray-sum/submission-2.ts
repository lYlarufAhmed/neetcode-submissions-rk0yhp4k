class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxAscendingSum(nums: number[]): number {
        let mSum = nums[0]
        let cSum = nums[0]
        for (let ind=1; ind < nums.length; ind++){
             if (nums[ind] > nums[ind-1]){
                cSum += nums[ind]
            } else {
                mSum = Math.max(mSum, cSum)
                cSum = nums[ind]
            }
        }



        return Math.max(mSum, cSum)
    }
}
