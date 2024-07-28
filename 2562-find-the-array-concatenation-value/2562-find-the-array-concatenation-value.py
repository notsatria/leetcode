class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0

        r = len(nums) - 1
        
        if len(nums) % 2 != 0:
            res = nums[len(nums) // 2]


        for i in range(len(nums)//2):
            print(res)

            conc = ""

            conc = str(nums[i]) + str(nums[r])

            res += int(conc)

            r -= 1

  

        return res