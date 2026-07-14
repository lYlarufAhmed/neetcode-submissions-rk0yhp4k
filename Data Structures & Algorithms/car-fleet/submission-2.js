class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let s_pos = position.toSorted((a,b)=> a-b)
        let lane = new Array(target).fill(0)
        position.map((s_p, i)=>{
            lane[s_p] = speed[i] 
            return s_p
        })
        s_pos = s_pos.map(p=> [p, lane[p]])
        let mrged = []
        while (s_pos.length > 1){
            let [p1, s1] = s_pos.pop()
            let temp = []
            while (s_pos.length){
                let [p2, s2] = s_pos.pop()
                if (s2 > s1 && (
                    (Math.abs(p2-p1) / Math.abs(s2-s1)) <= ((target-p1)/ s1)
                )){
                    continue
                }
                temp.push([p2, s2])
            }

            while (temp.length){
                s_pos.push(temp.pop())
            }
            mrged.push([p1,s1])
        }
        return s_pos.length + mrged.length
    }
}
