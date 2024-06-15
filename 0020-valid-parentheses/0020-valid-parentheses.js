/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
   const bracketStack = new Stack()
   
   for (let i = 0; i < s.length; i++) {
       const bracket = s[i]
       if (bracket === "(" || bracket === "{" || bracket === "[") {
           bracketStack.push(bracket)
       } else if (bracket === ")") {
           if (bracketStack.peek() === "(") {
               bracketStack.pop()
           } else {
               return false
           }
       } else if (bracket === "}") {
           if (bracketStack.peek() === "{") {
               bracketStack.pop()
           } else {
               return false
           }
       } else if (bracket === "]") {
           if (bracketStack.peek() === "[") {
               bracketStack.pop()
           } else {
               return false
           }
       }
   }

    if (bracketStack.size() === 0) {
        return true
    } else {
        return false
    }
};

class Stack {
    constructor() {
        this.items = []
    }
    
    push(element) {
        this.items.push(element)
    }
    
    pop() {
        if (this.items.isEmpty) {
            return "The stack is empty"
        }
        this.items.pop()
    }
    
    size() {
        return this.items.length
    }
    
    peek() {
        if (this.items.isEmpty) {
            return "The stack is empty"
        }
        return this.items[this.items.length - 1]
    }
    
    print() {
        console.log(this.items.toString())
    }
}