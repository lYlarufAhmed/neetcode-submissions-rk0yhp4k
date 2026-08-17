class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let seenMap = new Map()

        for (let ind in nums){

            //console.log(ind, Number(ind))
            let num = nums[ind]
            let compI = seenMap.get(String(num))
            if (compI !== undefined) return [compI, Number(ind)]
            let comp = target - num
            seenMap.set(String(comp), Number(ind))
        }
    }
}
