class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let newM = new Map()
        for (let i=0; i < nums.length; i++){
            let curr = nums[i]
            let comp = target-curr
            if (newM.has(curr)){
                return [i, newM.get(curr)]
            }else{
                newM.set(comp, i)
            }
        }
        
    }
}
