class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let mem = new Set()
        let index = 0
        nums.forEach((item, index) => {
        })

        while (index < nums.length) {
            let item = nums[index]
            if (mem.has(item)) return true
            mem.add(item)

            index++
        }

        return false
    }
}
