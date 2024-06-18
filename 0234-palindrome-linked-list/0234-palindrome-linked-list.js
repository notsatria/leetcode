/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let current = head;
    const list = [];
    let pointer = 1;
    
    while (current !== null) {
        console.log(current.val)
        list.push(current.val)
        current = current.next
    }
    
    for (let i = 0; i < Math.floor(list.length / 2); i++) {
        if (list[i] === list[list.length - pointer]) {
            pointer++
        } else {
            return false;
        }
    }
    
    return true
};