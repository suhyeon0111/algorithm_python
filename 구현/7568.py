# 덩치

from sys import stdin

n = int(stdin.readline())
build = []  # 덩치 리스트
result = []  # 결과 리스트

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    build.append((x, y))

for i in range(n):
    rank = 1
    for j in range(n):
        if build[i][0] < build[j][0] and build[i][1] < build[j][1]:  # 다른 사람이 덩치가 클 때
            rank += 1
    result.append(rank)

# 한 줄 출력
for x in result:
    print(x, end=" ")
