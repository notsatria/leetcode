/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const magazineMap = new Map()
    
    for (let i = 0; i < magazine.length; i++) {
        const char = magazine[i]
        if (magazineMap.has(char)) {
            magazineMap.set(char, magazineMap.get(char) + 1)
        } else {
            magazineMap.set(char, 1) 
        }
    }
    
    for (let i = 0; i < ransomNote.length; i++) {
        let char = ransomNote[i]
        
        if (!magazineMap.has(char) || magazineMap.get(char) === 0) {
            return false
        }
        
        magazineMap.set(char, magazineMap.get(char) - 1)
    }
    
    return true
};