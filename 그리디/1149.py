'''
RGB거리
'''

# 각 집의 R G B 비용
# 모든 집을 칠하는 비용의 최솟값
from sys import stdin

n = int(stdin.readline())
home = []
for i in range(n):
    home.append(list(map(int, input().split())))
    
for i in range(1, len(home)):
    home[i][0] = min(home[i - 1][1], home[i - 1][2]) + home[i][0]
    home[i][1] = min(home[i - 1][0], home[i - 1][2]) + home[i][1]
    home[i][2] = min(home[i - 1][0], home[i - 1][1]) + home[i][2]
print(min(home[n - 1][0], home[n - 1][1], home[n - 1][2]))