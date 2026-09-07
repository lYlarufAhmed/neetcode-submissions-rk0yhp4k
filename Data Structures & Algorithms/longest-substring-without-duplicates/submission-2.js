class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        /**
         * - 2 pointer
         * - sliding window
         */
        let seenHash = new Set();
        let l = 0,
            r = 0;
        let maxL = 0;
        while (r < s.length) {
            let c = s[r];
            while (seenHash.has(c)) {
                seenHash.delete(s[l]);
                l++;
            }

            maxL = Math.max(maxL, r - l + 1);
            seenHash.add(s[r]);
            r++;
        }

        // return r - l +1
        return maxL;
    }
}
