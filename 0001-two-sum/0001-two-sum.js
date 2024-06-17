/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const pairs = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (pairs.has(complement)) {
            return [pairs.get(complement), i];
        }
            
        pairs.set(nums[i], i);
    }
    
    return [];

};