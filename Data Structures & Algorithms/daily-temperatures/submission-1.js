class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let res = Array(temperatures.length).fill(0)
        let l = temperatures.length
        let st = []

        for (let i in temperatures){
            let curr = temperatures[i]
            while (st.length && curr > st[st.length-1][0]){
                let [_, ind] = st.pop()
                res[ind] = i - ind
            }
            st.push([curr, i])
        }

        return res
    }
}
