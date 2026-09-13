class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isSubsequence(s: string, t: string): boolean {
        let p1 = 0,
            p2 = 0;

        for (let i: number = 0; i < t.length; i++) {
            if (s[p1] == t[i]) p1++;
        }
        console.log(p1);
        return p1 == s.length;
    }
}
