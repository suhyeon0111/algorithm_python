# 추월

import sys

n = int(sys.stdin.readline())
start_number = {}  # 출발
arrive_number = []  # 도착
idx = 0  # 인덱스
for _ in range(n):
    start_number[sys.stdin.readline()] = idx
    idx += 1
for _ in range(n):
    arrive_number.append(sys.stdin.readline())


cnt = 0  # 추월 차량 수
for i in range(n - 1):
    for j in range(i + 1, n):
        if start_number[arrive_number[i]] > start_number[arrive_number[j]]:
            cnt += 1
            break

print(cnt)
