/*
    Cara paling gampangnya kan bruteforce, tapi itu O(n)

    Sekarang gimana caranya binary search?

    Binary kan artinya membagi menjadi 2 bagian. 

    Pertama, cari target apakah di tengah tengah nums?

    if (target == (nums.size / 2)) return nums.size / 2

    Berarti searchingnya adalah mulai dari 0 ke (nums.size / 2) - 1
    Sama dari nums.size / 2 ke nums.size - 1

    Ohiya, karena nums udah sorted, berarti tinggal bandingin apakah lebih besar lebih kecil dari target

    (selalu cari tengah tengah)
    Jadi jika target > nums[(nums.size / 2)] maka ambil bagian kanan, begitu sebaliknya.

    Lalu dari kanan itu bisa dibagi 2 lagi, 
 */
import kotlin.math.floor

class Solution {
    fun search(nums: IntArray, target: Int): Int {
        if (nums.size == 1) {
            if (target == nums[0]) return 0
            else return -1
        }
        var leftIndex = 0
        var rightIndex = (nums.size - 1)

        while (leftIndex <= rightIndex) {
            var mid = (rightIndex + leftIndex) / 2
            if (target > nums[mid]) {
                leftIndex = mid + 1
            } else if (target == nums[mid]) {
               return mid
            } else {
                rightIndex = mid - 1
            }
        }

        return -1
    }
}