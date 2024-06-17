/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const pairs = new Map();
    const result = [];
    
    for (let i = 0; i < nums.length; i++) {
        pairs.set(i, nums[i]);

        // for (let value of pairs.values()) {
        //     if (value === target - nums[i]) {
        //         console.log(value);
        //     }
        // }
        pairs.forEach((value, key) => {
            if (value === target - nums[i] && key != i) {
                console.log([key, i]);
                result.push(...[key, i])
            }
        })
    }
    
    return result;

};