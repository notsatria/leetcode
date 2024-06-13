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
    var temp = 0
    
    for (var i = 0; i < s.length; i++) {
        // console.log(result)
        console.log("result before: " + result)
        if (roman[s[i]] < roman[s[i + 1]]) {
            result = result + roman[s[i + 1]] - roman[s[i]]
            console.log("result inside temp: " + result)
            i++
        } else {
            result = result + roman[s[i]]
        }
        console.log("result after: " + result)

    }
    
    
    return result
};