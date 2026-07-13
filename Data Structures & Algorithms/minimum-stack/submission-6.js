class MinStack {
    constructor() {
        this.min = Infinity;
        this.arr = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        if (this.arr.length > 0) {
            this.arr.push(val - this.min);
            if (val < this.min) this.min = val;
        } else {
            this.min = val;
            this.arr.push(0);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        let p = this.arr.pop();
        if (p < 0) {
            this.min -= p;
        }
    }

    /**
     * @return {number}
     */
    top() {
        let t = this.arr[this.arr.length - 1];
        if (t > 0) return t + this.min;
        return this.min;
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min;
    }
}
