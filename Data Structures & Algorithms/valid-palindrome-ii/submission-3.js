class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    validPalindrome(s) {
        const isPalindromeRange = (i, j)=>{
            while (i < j){
                if (s[i] != s[j]) return false
                i++
                j--
            }
            return true
        }

        let l = 0,
        r = s.length - 1

        while (l < r){
            if (s[l] !== s[r]) return isPalindromeRange(l+1, r) || isPalindromeRange(l, r-1)
            l++
            r--
        }

        return true
    }
}
