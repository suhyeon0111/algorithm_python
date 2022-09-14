# 개미굴

import sys

n = int(sys.stdin.readline())
food_infomation = []
for _ in range(n):
    infomation = list(sys.stdin.readline().rsplit())
    food_infomation.append(infomation[1:])  # 숫자 제거

food_infomation.sort()

floor = "--"
result = []
for i in range(n):
    if i == 0:
        for j in range(len(food_infomation[i])):
            result.append(floor * j + food_infomation[i][j])
    else:
        idx = 0  # 같은 원소의 개수 저장
        for j in range(len(food_infomation[i])):
            if food_infomation[i - 1][j] != food_infomation[i][j] or len(food_infomation[i - 1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(food_infomation[i])):
            result.append(floor * j + food_infomation[i][j])

for x in result:
    print(x)
