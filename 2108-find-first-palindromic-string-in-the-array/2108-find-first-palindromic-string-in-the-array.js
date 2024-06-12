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

    if (inputString.length === 1 ) {
        return true;
    }
    
    var list = []
    
    for (var i = 0; i < inputString.length; i++) {
        list.push(inputString[i])
    }
    
    var reversedList = list.slice().reverse()
    
    if (reversedList.length == list.length) {
         
    for (var i = 0; i < reversedList.length; i++) {
            if (reversedList[i] !== list[i]) {
                return false
            } 
        
        }
    
    }
    
    
    return true
}