/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map()
    const result = []
    
    for (let i = 0; i < strs.length; i++) {
        let sortedWord = strs[i].split("").sort().join("")
        if (!map.has(sortedWord)) {
            map.set(sortedWord, [strs[i]])
        } else {
            map.get(sortedWord).push(strs[i])
        }
    }
    
    for (value of map.values()) {
        result.push(value)
    }
    
    return result

};
