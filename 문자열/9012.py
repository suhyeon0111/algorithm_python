# 괄호

from sys import stdin

t = int(stdin.readline())

p = []
for _ in range(t):
    parentheses = stdin.readline()
    p.append(parentheses)

    cnt = 0
    stack = []
    for s in parentheses:
        if s == '(':
            stack.append('(')
        if s == ')':
            if stack:
                stack.pop()
            else:
                stack.append(')')
                break

    if not stack:
        print("YES")
    else:
        print("NO")
