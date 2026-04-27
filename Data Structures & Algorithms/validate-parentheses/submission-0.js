class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const opening = '({['
        const mapping = {
            '{':'}',
            '[':']',
            '(':')'
        }
        const stack = []

        for (let c of s){
            if (opening.includes(c)){
                stack.push(mapping[c])
            }else{
                const last = stack.pop()
                if (last !== c) return false
            }
        }
        return stack.length == 0
    }
}
