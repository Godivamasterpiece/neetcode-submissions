class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(','{','[']
        close = [')','}',']']
        stack = []
        for char in s:
            if char in openers:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                stackpop = stack.pop()
                if char == '}' and stackpop == '{':
                    continue
                if char == ')' and stackpop == '(':
                    continue
                if char == ']' and stackpop == '[':
                    continue
                return False
        if len(stack) > 0:
            return False
        return True