'''
행복 유치원 문제
가장 키가 큰 원생 - 가장 키가 작은 원생
'''

from sys import stdin

n, k = map(int, stdin.readline().split()) # 유치원 생의 수 n, 조의 개수 k
child = list(map(int, stdin.readline().split()))  # 유치원 생들의 키

d = []  # 키 차이를 저장할 리스트
for i in range(1, n):
    d.append(child[i] - child[i - 1])
d.sort()

cost = 0
if k == n:  # 각 1명씩 조를 이루게 될 때
    print(0)
else:
    for i in range(n - k):  # 조 개수 만큼 for 루프 돌기  
        cost += d[i]  
    print(cost)

    