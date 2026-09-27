/**
 * const PriorityQueue = require('priority-queue-js');
 */

class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @param {number} src
     * @returns {Object}
     */
    shortestPath(n, edges, src) {
        const adj = Array.from({ length: n }, () => []);
        const shortest = {};

        for (let [s, d, w] of edges) {
            adj[s].push([d, w]);
        }
        const minHeap = new PriorityQueue((a, b) => a[0] - b[0]);
        minHeap.enqueue([0, src]);

        while (!minHeap.isEmpty()) {
            let [w1, n1] = minHeap.dequeue();

            if (n1 in shortest) {
                continue;
            }

            shortest[n1] = w1;

            for (const [n2, w2] of adj[n1]) {
                if (!(n2 in shortest)) {
                    minHeap.enqueue([w1 + w2, n2]);
                }
            }
        }

        for (let i = 0; i < n; i++) {
            if (!(i in shortest)) shortest[i] = -1;
        }

        return shortest;
    }
}
