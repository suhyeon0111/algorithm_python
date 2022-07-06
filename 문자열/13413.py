# 오셀로 재배치

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    initial_state = list(map(str, stdin.readline().rstrip()))
    target_state = list(map(str, stdin.readline().rstrip()))
    cnt = []

    for i in range(n):
        if initial_state[i] != target_state[i]:
            cnt.append(initial_state[i])

    if not cnt:
        print(0)

    elif cnt.count("B") >= cnt.count("W"):
        print(cnt.count("B"))

    else:
        print(cnt.count("W"))
