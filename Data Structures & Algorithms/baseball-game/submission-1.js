class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        return operations.reduce((acc, curr)=> {
            if (curr == '+'){
                const [a, b] = acc.slice(-2)
                acc.push(a+b)
                return acc
            }
            else if (curr == 'C'){
                acc.pop()
                return acc
            }
            else if (curr == 'D'){
                const b = acc.slice(-1)[0]
                acc.push(2*b)
                return acc
            }else{
                acc.push(Number(curr))
                return acc
            }
        }, [])
        .reduce((acc, curr)=> acc + curr, 0)
    }
}
