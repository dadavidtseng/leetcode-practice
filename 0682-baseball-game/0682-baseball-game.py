class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []

        for operation in operations:
            if operation == "+":
                result.append(result[-1] + result[-2])
            elif operation == "C":
                result.remove(result[-1])
            elif operation == "D":
                result.append(result[-1] * 2)
            else:
                result.append(int(operation))
        return sum(result)
