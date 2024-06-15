/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
   const bracketStack = new Stack()
   const brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    };
   
   for (let i = 0; i < s.length; i++) {
       const bracket = s[i]
       
       if (brackets[bracket]) {
           // jika bracket adalah opening
           bracketStack.push(bracket)
       } else {
           // jika bracket adalah penutup
           // check apakah last item di dalam stack adalah pembuka dari penutup
           const lastBracket = bracketStack.pop()
           console.log(lastBracket)
           if (brackets[lastBracket] !== bracket) {
               return false
           }
       }
   }

    return bracketStack.isEmpty()
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
        return this.items.pop()
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
    
    isEmpty() {
        return this.items.length === 0
    }
    
    print() {
        console.log(this.items.toString())
    }
}