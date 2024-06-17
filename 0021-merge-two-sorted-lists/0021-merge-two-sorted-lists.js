/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // ListNode1 = [Node(1), Node(2), Node(4)]
    // ListNode2 = [Node(1), Node(3), Node(4)]
    // hasil seharusnya
    // ListNode 3 = [Node(1), Node(1), Node(2), Node(3), Node(4), Node(4)]

    let dummy = new ListNode()
    let current = dummy
    
    while (list1 !== null && list2 !== null) {
        if (list1.val > list2.val) {
            current.next = list2
            list2 = list2.next
        } else {
            current.next = list1
            list1 = list1.next
        }
        current = current.next
    }
    
    if (list1 !== null) {
        current.next = list1
    } else {
        current.next = list2
    }
    
    return dummy.next

};
