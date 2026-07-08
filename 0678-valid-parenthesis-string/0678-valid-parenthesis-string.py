class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for idx, c in enumerate(s):
            if c == "(":
                left_stack.append(idx)
            elif c == "*":
                star_stack.append(idx)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False
        return not left_stack
