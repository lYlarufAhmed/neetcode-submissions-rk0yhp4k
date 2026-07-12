class MinStack {
    constructor() {
        this.stack = []
        this.mini = []
        this.min = Infinity
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        if (this.mini.length == 0 || val<this.mini[this.mini.length-1]){
            this.mini.push(val)
        } 
        else{
            this.mini.push(this.mini[this.mini.length-1])
        }
    }

    /**
     * @return {void}
     */
    pop() {
        console.log(this.stack)
        console.log(this.mini)
        if (this.stack.length){
            this.stack.pop()
            this.mini.pop()
        } 
    }

    /**
     * @return {number}
     */
    top() {
        if (this.stack.length) return this.stack[this.stack.length-1]
    }

    /**
     * @return {number}
     */
    getMin() {
        if (this.mini.length) return this.mini[this.mini.length-1]
    }
}
