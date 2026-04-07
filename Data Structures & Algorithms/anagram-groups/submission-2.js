class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const alpha = "abcdefghijklmnopqrstuvwxyz"
        let maskMap = new Map()
        const createWordMask = word => {
            let mask = new Array(26).fill(0)
            for (const c of word){
                const alI = alpha.indexOf(c)
                const count = mask[alI]
                // console.log('index of ', c, ' => ', alI, ' count ', count)
                mask[alI] = count + 1
            }

            // console.log('final mask ', mask)
            return mask.join(',')
        }

        for (const str of strs){
            const wordMask = createWordMask(str)
            const existingMask = maskMap.get(wordMask)
            if (existingMask){
                maskMap.set(wordMask, [...existingMask, str])
            }else{
                maskMap.set(wordMask, [str])
            }
        }
        // console.log(maskMap)
        return [...maskMap.values()]
    }
}
