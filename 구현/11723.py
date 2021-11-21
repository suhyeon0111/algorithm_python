'''
<집합>

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 

'''

import sys

m = int(sys.stdin.readline())
s = []
result = []

for _ in range(m):
    answer = sys.stdin.readline().strip().split()

    if len(answer) == 1:
        if answer[0] == 'all':
            # all일 때 
            s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        
        if answer[0] == 'empty':
            # all일 때 
            s = []

    else:
        order, x = answer[0], answer[1]

        if order == 'add':
            if not x in s:
                s.append(x)
        
        elif order == 'remove':
            if x in s:
                # print(1)
                s.remove(x)
        
        elif order == 'check':
            if x in s:
                # print(1)
                result.append(1)
            else:
                # print(0)
                result.append(0)

        elif order == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.append(x)

for i in result:
    print(i)