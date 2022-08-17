# 인사성 밝은 곰곰이
# 시간초과

from sys import stdin

n = int(stdin.readline())
stack = []
cnt = 0
for _ in range(n):
    enter = stdin.readline()
    if enter == 'ENTER':
        stack.clear()
    elif enter not in stack:
        stack.append(enter)
        cnt += 1


print(cnt)
