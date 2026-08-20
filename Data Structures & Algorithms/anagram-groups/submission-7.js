class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let m = new Map();
        strs.map((str, i) => [str.split("").sort().join(""), str])
            /*.sort(([s, i], [s1, i1]) => {
                if (s < s1) {
                    return -1;
                }
                if (s > s1) {
                    return 1;
                }

                // names must be equal
                return 0;
            })*/
            .forEach(([key, val]) => {
                let curr = m.get(key) || [];
                curr.push(val);
                m.set(key, curr);
            });
        return Array.from(m.values());
    }
}
