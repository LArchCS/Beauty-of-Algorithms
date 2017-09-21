# CS 21A
# PS 1 Q4 - postFix
# pseudo code test in Python

def postFix(s):
    stack = []
    res = ""
    for i in range(0, len(s)):
        char = s[i]
        if 48 <= ord(char) <= 57 or 96 < ord(char) < 123 or 64 < ord(char) < 91:
            res += char
            if len(stack) > 0 and stack[-1] in '+-*/':
                res += stack.pop()
        elif char == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            if len(stack) > 0 and stack[-1] in '+-*/' and char in "+-*/":
                res += stack.pop()
            stack.append(char)
    if len(stack) > 0:
        res += stack.pop()
    return res


# TEST

s = '5+((1+2)*4)-3'
print postFix(s)

s = '(a+(b*c))*d'
print postFix(s)

s = '3-4+5'
print postFix(s)

s = '3-(4*5)'
print postFix(s)

s = '1+5*7'
print postFix(s)