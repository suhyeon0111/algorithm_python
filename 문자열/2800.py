# 괄호 제거

import sys
from itertools import combinations

word = sys.stdin.readline().rstrip()

stack = []
l = []  # 괄호 인덱스 위치 넣을 리스트
result = set()  # 중복 제거

for i, x in enumerate(list(word)):
    if x == '(':
        stack.append(i)
    elif x == ')':
        start = stack.pop()
        end = i
        l.append([start, end])

for i in range(1, len(l)+1):
    combi = combinations(l, i)
    for j in combi:
        tmp = list(word)
        for k in j:
            start, end = k  # 괄호쌍의 인덱스
            tmp[start] = ''
            tmp[end] = ''  # 괄호 쌍 없애기
        result.add(''.join(tmp))


for i in sorted(result):
    print(i)
