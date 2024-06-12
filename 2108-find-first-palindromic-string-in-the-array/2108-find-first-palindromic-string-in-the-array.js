/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    for (var i = 0; i < words.length; i++) {
        if (isPalindrome(words[i])) {
            return words[i];
        } 
    }
    return "";
};

function isPalindrome(inputString) {
    const len = inputString.length

    for (var i = 0; i < Math.floor(len/2); i++) {
            if (inputString[i] !== inputString[len - 1 - i]) {
                return false
            } 
        
        }
    
    return true
}