# 개미굴

import sys

n = int(sys.stdin.readline())
food = []
for _ in range(n):
    infomation = list(sys.stdin.readline().split())
    food.append(infomation[1:])

food.sort()

result = []  # 결과값 저장
dash = "--"  # 층 나타내기

for i in range(n):
    if i == 0:  # 처음은 중복이 없으므로 바로 append
        for j in range(len(food[i])):
            result.append(dash * j + (food[i][j]))
