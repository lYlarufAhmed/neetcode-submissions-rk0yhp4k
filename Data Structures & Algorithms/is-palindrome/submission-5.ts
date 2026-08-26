class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {

        let s_l = s.toLowerCase();
        s.charCodeAt(0);
        const isAlpha = (code: number) =>
            (code >= 97 && code <= 122) || (code >= 65 && code <= 90) || (code >= 48 && code <= 57);

        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            if (isAlpha(s.charCodeAt(l)) && isAlpha(s.charCodeAt(r))) {
                if (s_l[l] == s_l[r]) {
                    l++;
                    r--;
                    continue;
                } else {
                    return false;
                }
            } else if (!isAlpha(s.charCodeAt(l))) l++;
            else if (!isAlpha(s.charCodeAt(r))) r--;
        }
        return true;
    }
}
