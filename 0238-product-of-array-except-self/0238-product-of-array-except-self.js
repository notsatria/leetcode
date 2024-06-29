/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const length = nums.length
    const prefix = Array.from({ length }, () => 1)
    const postfix = Array.from({ length }, () => 1)
    const answer = Array.from({ length }, () => 1)

    
    for (let i = 0; i < length; i++) {
        if (i === 0) {
            prefix[i] = prefix[i] * nums[i]
        } else {
            prefix[i] = prefix[i - 1] * nums[i]        
        }
    }
    
    for (let i = length - 1; i >= 0; i--) {
        if (i === length - 1) {
            postfix[i] = postfix[i] * nums[i]        
        } else {
            postfix[i] = postfix[i + 1] * nums[i]        
        }
    }
    
    console.log(prefix)
    console.log(postfix)
    
    for (let i = 0; i < length; i++) {
        if (i === 0) {
            answer[i] = postfix[i + 1]
        } else if (i === length - 1) {
            answer[i] = prefix[i - 1]
        } else {
            answer[i] = prefix[i - 1] * postfix[i + 1]
        }
    }
    
    console.log(answer)
    return answer
};