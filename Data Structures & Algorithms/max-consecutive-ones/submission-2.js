class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let maxC = 0
        let acc = nums.reduce((acc, currVal)=> {
            if (currVal === 0){
                maxC = Math.max(maxC, acc)
                return 0
            }else return acc+1
        }, 0)

        return Math.max(maxC, acc)
    }
}
