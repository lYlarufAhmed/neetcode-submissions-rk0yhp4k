class MinStack {
    constructor() {
        this.arr = [];
        this.mini = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.arr.push(val);
        if (this.mini.length == 0 || this.mini[this.mini.length - 1] > val) {
            this.mini.push(val);
        } else {
            this.mini.push(this.mini[this.mini.length - 1]);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.arr.pop();
        this.mini.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.arr[this.arr.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.mini[this.mini.length - 1];
    }
}
