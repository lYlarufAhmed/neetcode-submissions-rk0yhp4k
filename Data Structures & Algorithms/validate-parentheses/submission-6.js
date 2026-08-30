class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let dict = new Map([
            ["{", "}"],
            ["(", ")"],
            ["[", "]"],
        ]);
        let stack = [];

        for (let c of s) {
            if (dict.has(c)) stack.push(dict.get(c));
            else if (c !== stack.pop()) return false;
        }
        return stack.length == 0;
    }
}
