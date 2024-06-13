/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    var result = 0
    
    for (var i = 0; i < s.length; i++) {
        if (i < s.length -1 && roman[s[i]] < roman[s[i + 1]]) {
            result -= roman[s[i]]
        } else {
            result += roman[s[i]]
        }
    }
    
    
    return result
};