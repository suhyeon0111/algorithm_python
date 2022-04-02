# -*- coding: utf-8 -*- 
# 병든 나이트

from sys import stdin

n, m = map(int, stdin.readline().split())

if n == 1:  # 세로가 최소 2는 되어야 움직일 수 있음
    print(1)
elif n == 2:  # 2, 3번 가능/ 이동횟수가 4보다 적지 않은 경우를 고려해야 함
    print(min(4, (m + 1) // 2))  # 예시) m = 5일때, 방문한 칸 3
else:  # 세로가 3이상
    if m <= 6:  # 가로가 6이하 -> 1, 4번 가능
        print(min(4, m))
    else:  # 가로가 6이상 -> 모든 방법 다 써야함
        print(m - 2)