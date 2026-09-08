class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []

        for bracket in s:
            if bracket == "(":
                stack.append(")")
            elif bracket == "[":
                stack.append("]")
            elif bracket == "{":
                stack.append("}")
            elif len(stack) > 0 and bracket == stack[-1]:
                stack.pop()
            else:
                return(False)
        if len(stack) > 0:
            return(False)
        else:
            return(True)