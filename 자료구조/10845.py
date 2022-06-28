# 큐
from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque([])

for i in range(n):
    order = stdin.readline().split()

    if order[0] == 'push':  # 큐에 넣음/ 출력은 하지 않음
        queue.append(order[1])

    elif order[0] == 'pop':
        if len(queue) == 0:  # 큐에 아무것도 들어있지 않으면
            print(-1)
        else:
            print(queue.popleft())

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':  # 큐가 비어있으면 1 아니면 0
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':  # 큐의 가장 앞 정수 출력/ 없으면 -1
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif order[0] == 'back':  # 큐의 가장 뒤에 있는 정수 출력/ 없으면 -1
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
