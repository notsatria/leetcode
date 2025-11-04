class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        nums.sorted()
        val existing = hashMapOf<Int, Int>()
        for (item in nums) {
            if (existing.containsKey(item)) {
                return true
            }
            existing.put(item, (existing.get(item) ?: 0) + 1)
        }
        return false
    }
}