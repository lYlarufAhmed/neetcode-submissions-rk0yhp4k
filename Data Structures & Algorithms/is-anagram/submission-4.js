class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let seenMap = new Map()

        for (let c of s){
            let count = seenMap.get(c) || 0
            seenMap.set(c, count+1)
        }

        for (let c of t){
            let count = seenMap.get(c) || 0
            if (count == 0) return false
            else if (count == 1) seenMap.delete(c)
            else seenMap.set(c, count-1)
        }
        console.log(seenMap.keys().next())
        return seenMap.keys().next().value === undefined
    }
}
