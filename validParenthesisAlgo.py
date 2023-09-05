"""The algorithm for validating parentheses in an expression is commonly referred
to as the "Valid Parentheses" algorithm. It's a well-known problem in computer science
and is often used to check if the arrangement of parentheses (such as parentheses,
square brackets, and curly braces) in an expression is valid or not.
"""

def validParenthesis(expression):
        stack = []
        parenDict = {"}" : "{", ")" : "(", "]" : "["}
        for parenthesis in expression:
            if parenthesis not in parenDict.keys():
                stack.append(parenthesis)
            else:
                if stack and stack[-1] ==  parenDict[parenthesis]:
                    stack.pop()
                else:
                    return False
        return not stack
