class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let res = Array(temperatures.length).fill(0)
        let st = []

        for (let i = temperatures.length-2; i > -1 ; i--){
            let [curr, next] = temperatures.slice(i, i+2)
            if (curr < next){
                res[i] = 1
            }
            else{
                let count = 1
                for (let j = i+2; j < temperatures.length; j++, count++){
                    if (temperatures[j] > curr){
                        res[i] = ++count
                        break;
                    }
                }
            }
        }

        return res
    }
}
