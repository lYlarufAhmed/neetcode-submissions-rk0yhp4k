class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let set_1 = new Map()
        let set_2 = new Map()
        if (s.length != t.length) return false


        for (let i=0;i<s.length; i++){
            let count = 1
            if (set_1.has(s[i])){
                count = set_1.get(s[i])+1
            }
            set_1.set(s[i], count)
        }

        for (let i=0;i<t.length; i++){
            let count = 1
            if (set_2.has(t[i])){
                count = set_2.get(t[i])+1
            }
            set_2.set(t[i], count)
        }
        console.log(set_1, set_2)
        for (const [key, val] of set_1.entries()){

            console.log(key, val)
            if (set_2.get(key) != val) return false
        }

        return true

        
    }
}
