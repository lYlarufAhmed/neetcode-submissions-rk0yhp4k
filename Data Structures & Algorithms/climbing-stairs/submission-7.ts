class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n: number): number {
        if ( n <= 3) return n

        let prev = 2
        let curr = 3
        let count = 4

        while (count <= n){

            [curr, prev] = [curr + prev, curr]
            console.log({count, curr, prev})

            count++

            
        }
        return curr
    }
}
