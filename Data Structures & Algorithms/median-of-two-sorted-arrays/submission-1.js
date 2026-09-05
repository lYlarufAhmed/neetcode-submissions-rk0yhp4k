class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let total_len = nums1.length + nums2.length;
        let med;
        med = total_len / 2;

        let comb_arr = [];
        let i = 0,
            j = 0;

        while (comb_arr.length < med + 1) {
            if (i < nums1.length && j < nums2.length) {
                if (nums1[i] < nums2[j]) {
                    comb_arr[comb_arr.length] = nums1[i];
                    i++;
                } else {
                    comb_arr[comb_arr.length] = nums2[j];
                    j++;
                }
            } else if (i < nums1.length) {
                comb_arr[comb_arr.length] = nums1[i];
                i++;
            } else {
                comb_arr[comb_arr.length] = nums2[j];
                j++;
            }
        }

        console.log(comb_arr);
        if (total_len % 2) {
            return comb_arr[Math.floor(med)];
        } else {
            return comb_arr.slice(-2).reduce((acc, curr) => acc + curr, 0) / 2;
        }
    }
}
