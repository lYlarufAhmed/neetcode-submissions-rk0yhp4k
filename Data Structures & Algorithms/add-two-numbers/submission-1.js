/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        let result = new ListNode();
        let curr_l1 = l1;
        let curr_l2 = l2;
        let curr_result = result;

        let carry = 0;

        while (true) {
            let s = (curr_l1?.val ?? 0) + (curr_l2?.val ?? 0) + carry;
            console.log(s);
            curr_result.val = s % 10;
            carry = Math.floor(s / 10);

            curr_l1 = curr_l1?.next;
            curr_l2 = curr_l2?.next;
            if (curr_l1 || curr_l2) {
                curr_result.next = new ListNode();
                curr_result = curr_result.next;
            } else {
                if (carry) curr_result.next = new ListNode(carry);
                break;
            }
        }

        return result;
    }
}
