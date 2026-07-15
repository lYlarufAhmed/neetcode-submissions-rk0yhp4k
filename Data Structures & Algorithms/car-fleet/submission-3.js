class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let s_pos = position.map((p, i) => [p, speed[i]]);
        s_pos.sort((a, b) => b[0] - a[0]);
 //       console.log(s_pos)

        let times = [];
        for (let i = 0; i < s_pos.length; i++) {

            let [p, s] = s_pos[i]
            let t = (target-p) / s

            if (!times.length || t > times[times.length-1]){
               times.push(t) 
            }

        }
//        console.log(times)
        return times.length;
    }
}
