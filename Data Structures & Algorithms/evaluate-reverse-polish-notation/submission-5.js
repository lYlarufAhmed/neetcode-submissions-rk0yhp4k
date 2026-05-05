class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let currStack = [];

        for (let p of tokens) {
            // console.log(p);
            let parsed = Number.parseInt(p);
            if (!Number.isNaN(parsed)) {
                currStack.push(parsed);
            } else {
                // its a operator
                console.log(currStack);
                let [d1, d2] = [currStack.pop(0), currStack.pop(0)];
                console.log(`${d2}${p}${d1}`);
                const res = eval(`${d2}${p}(${d1})`);
                console.log(res);
                currStack.push(p === "/" ?  (res < 0 ? Math.ceil(res): Math.floor(res)) : res);
            }
        }
        return currStack.pop();
    }
}
