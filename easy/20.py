# 20. Valid Parentheses solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(","]": "[","}": "{"}
        for i in s:
            if i in pair:
                if stack and stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
