/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    
    for (var i = 0; i < nums.length; i++) {
        map.set(nums[i], i);
    }
    
    for (var i = 0; i < nums.length; i++) {
        var complement = target - nums[i];
        
        if (map.has(complement) && (map.get(complement) !== i)) {
            return [i, map.get(complement)];
        }
    }
    
};