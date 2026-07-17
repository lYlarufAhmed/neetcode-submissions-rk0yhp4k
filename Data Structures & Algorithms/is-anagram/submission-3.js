class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let [s_l, t_l] = [s.length, t.length];
        if (s_l !== t_l) return false;
        let n_map = new Map();

        for (let c of s) {
            if (n_map.has(c)) n_map.set(c, n_map.get(c) + 1);
            else n_map.set(c, 1);
        }
        console.log(n_map)
        for (let c of t) {
            if (n_map.has(c) && n_map.get(c) > 0) n_map.set(c, n_map.get(c) - 1);
            else return false;
        }

        console.log(n_map)
        if (n_map.values().some((p) => p !== 0)) return false;
        return true;
    }
}
