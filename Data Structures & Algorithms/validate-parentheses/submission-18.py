class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []

        for b in s:
            if b in close_to_open:
                if stack and stack[-1] == close_to_open[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False