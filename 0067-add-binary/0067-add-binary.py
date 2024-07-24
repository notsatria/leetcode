class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = self.convertBinaryToInt(a) + self.convertBinaryToInt(b)
        return self.convertIntToBinary(result)

    def convertBinaryToInt(self, s: str) -> int:
        total = 0
        s = s[::-1]
        for i in range(len(s)):
            if s[i] == "1":
                total += 2 ** i

        return total

    def convertIntToBinary(self, num: int) -> str:
        if num == 0:
            return "0"
        result = ""

        while num > 0:
            result = str(num % 2) + result
            num = num // 2

        return result 