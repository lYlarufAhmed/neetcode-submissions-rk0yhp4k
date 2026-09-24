class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        let map_t = new Map();
        let res = new Map();
        let min_length = Infinity;
        for (let c of t) {
            map_t.set(c, (map_t.get(c) || 0) + 1);
        }
        let have = 0;
        let map_w = new Map();
        let left = 0,
            right = 0;
        while (right < s.length) {
            //console.log({ right });
            let rc = s[right];
            if (t.includes(rc)) {
                map_w.set(rc, (map_w.get(rc) || 0) + 1);
                if (map_t.get(rc) == map_w.get(rc)) {
                    have++;
                }
                //console.log(map_w);

                while (have >= map_t.size) {
                    // try to shrink
                    let len = right - left + 1;
                    min_length = Math.min(min_length, len);
                    if (min_length == len) res.set(len, [left, right + 1]);

                    let lc = s[left];
                    if (t.includes(lc)) {
                        map_w.set(lc, map_w.get(lc) - 1);
                        if (map_t.get(lc) > map_w.get(lc)) {
                            have--;
                        }
                    }
                    left++;
                }
 //               console.log(res);
            }
            right++;
        }
        // find the first instance of  t
        // try to optimize it by moving the left pointer
        // record the min of right - legt range
        // then move the left:right range to find another instance
        // repeat right <= last index

//        console.log(res);

        return min_length == Infinity ? "" : s.substring(...res.get(min_length));
    }
}
//
