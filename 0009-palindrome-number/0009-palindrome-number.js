/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let stringX = x.toString()
    let pointer = 1
    
    for (let i = 0; i < Math.floor(stringX.length / 2); i++) {
        if (stringX[i] === stringX[stringX.length - pointer]) {
            pointer++
        } else {
            return false
        }
    }
    
    return true
};