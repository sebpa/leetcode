class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        opening_brackets = {"[", "{", "("}
        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if not stack or not matching_brackets[stack.pop()] == bracket:
                    return False
        return False if stack else True
