
"""
과자 나눠주기

명절이 되면, 홍익이 집에는 조카들이 놀러 온다.  떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.

조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.

그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.

M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.

단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

"""


import sys

M, N = map(int, input().split())   #M:조카의 수, N: 과자의 수
snack_length = list(map(int, sys.stdin.readline().split())) #과자의 길이

start, end = 0, max(snack_length)
k = 0


while start <= end:
    mid = (start + end) // 2 #중간값
    cnt = 0

    if mid == 0:#중간값이 0이라면 나눠줄 수 없다고 판단하여 루프 탈출
        break

    for i in snack_length:
        if i >= mid: #기존 쿠키가 더 길다면
            cnt += (i // mid) #쿠키자르기

    if cnt >= M: #짧게 잘랐다고 판단
        start = mid + 1
        k = mid

    else:
        end = mid - 1


print(k)
