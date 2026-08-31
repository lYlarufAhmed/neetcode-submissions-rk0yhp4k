class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let seen = new Map();

        for (let c of s) {
            if (seen.has(c)) seen.set(c, seen.get(c) + 1);
            else seen.set(c, 1);
        }

        for (let c of t) {
            if (seen.has(c)) {
                let count = seen.get(c);
                if (count == 1) seen.delete(c);
                else seen.set(c, count - 1);
            } else {
                return false;
            }
        }
        //console.log(seen.keys.length);
        

        return seen.keys().toArray().length == 0;
    }
}
