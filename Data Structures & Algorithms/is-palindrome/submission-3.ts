class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let chars = "abcdefghijklmnopqrstuvwxyz0123456789";

        let s_l = s.toLowerCase();

        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            if (chars.includes(s_l[l]) && chars.includes(s_l[r])) {
                if (s_l[l] == s_l[r]) {
                    l++;
                    r--;
                    continue;
                } else {
                    return false;
                }
            } else if (!chars.includes(s_l[l])) l++;
            else if (!chars.includes(s_l[r])) r--;
        }
        return true
    }
}
