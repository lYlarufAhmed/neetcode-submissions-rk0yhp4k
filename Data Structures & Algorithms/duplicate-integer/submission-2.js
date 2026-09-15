class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */I
    hasDuplicate(nums) {
        let seenMap = new Set()
        for (let num of nums){
            if (seenMap.has(num)) return true
            else seenMap.add(num)
        }
        return false
    }
}
