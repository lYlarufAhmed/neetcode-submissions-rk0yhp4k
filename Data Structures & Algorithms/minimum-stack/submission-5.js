class MinStack {
    constructor() {
        this.arr = [];
        this.min = Infinity;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        if (this.arr.length === 0) {
            this.arr.push(0);
            this.min = val;
        } else {
            this.arr.push(val - this.min);
            if (val < this.min) this.min = val;
        }
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.arr.length) {
            let enc = this.arr.pop();
            if (enc < 0) {
                this.min = this.min - enc;
            }
        }
    }

    /**
     * @return {number}
     */
    top() {
        if (this.arr[this.arr.length - 1] >= 0) {
            // return the encoded value
            return this.min + this.arr[this.arr.length - 1];
        }
        // top value is min
        else return this.min;
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min;
    }
}
