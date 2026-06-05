class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let start = 0;
        let end = s.length - 1;
        const isAlphNum = (c) => {
            let cCode = c.charCodeAt(0);
            console.log(cCode, c)
            return (cCode >= 48 && cCode <= 57) || (cCode >= 97 && cCode <= 122);
        };
        const lc = s.toLowerCase()

        while (start <= end) {
            let sc = lc[start].toLowerCase();
            let ec = lc[end].toLowerCase();
            console.log(sc, ec, start, end);
            while (start < end && !isAlphNum(sc)) {
                start++;
                sc = lc[start].toLowerCase();
            }
            while (start < end && !isAlphNum(ec)) {
                end--;
                ec = lc[end].toLowerCase();
            }
            if (sc != ec) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
