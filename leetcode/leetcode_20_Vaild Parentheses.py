class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '{':
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif s[i] == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif s[i] == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True

