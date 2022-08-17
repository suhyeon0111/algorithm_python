# 소프트 사이드
import sys

n = sys.stdin.readline().strip()

result = []
for x in n:
    result.append(int(x))

result.sort(reverse=True)

for i in result:
    print(i, end='')
