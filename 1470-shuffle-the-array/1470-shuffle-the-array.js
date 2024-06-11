/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var l1 = []
    var l2 = []
    var result = []
    
    for (var i = 0; i < nums.length; i++) {
        l1.push(nums[i])
        if (l1.length == n) {
            break
        }
    }
    
    for (var i = n; i < nums.length; i++) {
        l2.push(nums[i])
        if (l2.length == n) {
            break
        }
    }
    
    for (var i = 0; i < n;  i++) {
        result.push(l1[i])
        result.push(l2[i])
    }
    
    return result
};