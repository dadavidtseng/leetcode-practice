class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1_size = len(num1)
        num2_size = len(num2)
        result = [0] * (num1_size + num2_size)
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(num1_size):
            for i2 in range(num2_size):
                digit = int(num1[i1]) * int(num2[i2])
                result[i1 + i2] += digit
                result[i1 + i2 + 1] += result[i1 + i2] // 10
                result[i1 + i2] = result[i1 + i2] % 10

        result = result[::-1]
        return "".join(map(str, result)).lstrip("0")
