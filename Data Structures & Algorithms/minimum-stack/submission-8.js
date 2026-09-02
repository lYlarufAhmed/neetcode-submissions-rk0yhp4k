class MinStack {
    constructor() {
        this.min_s = [];
        this.stack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.min_s.length === 0) this.min_s.push(val);
        else this.min_s.push(Math.min(val, this.min_s[this.min_s.length - 1]));
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop();
        this.min_s.pop();
    }

    /**
     * @return {number}
     */
    top() {
        if (this.stack.length) return this.stack.slice(-1)[0];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min_s.slice(-1)[0];
    }
}
