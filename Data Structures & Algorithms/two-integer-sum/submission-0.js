class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map()

        let i=0
        while(i < nums.length){
            let curr = nums[i]
                let diff = target-curr
              let  diffI = map.get(diff)
              
            if (diffI != undefined) {
                return [diffI, i]
            }
            map.set(curr, i)

            i++
        }
    }
}
