class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let p_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        };
        let st = [];
        if (s.length % 2) return false;

        for (let c of s) {
            if (p_map.hasOwnProperty(c)) {
                st.push(p_map[c]);
            } else {
                let last = st.pop();
                if (c != last) return false;
            }
        }
        return st.length == 0;
    }
}
//
