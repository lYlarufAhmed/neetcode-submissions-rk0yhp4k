class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    romanToInt(s) {
        let map = new Map([
            ["I", 1],
            ["V", 5],
            ["X", 10],
            ["L", 50],
            ["C", 100],
            ["D", 500],
            ["M", 1000],
        ]);

        let val = map.get(s[s.length - 1]);

        for (let i = s.length - 2; i > -1; i--) {
            let [curr, prev] = [map.get(s[i]), map.get(s[i + 1])];
            if (curr < prev) val -= curr
            else val += curr

        }
        return val

    }
}
