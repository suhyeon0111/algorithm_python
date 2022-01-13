'''
A -> B

1. 2 곱하기
2. 뒤에 1붙이기
'''


from sys import stdin

a, b = map(int, stdin.readline().split())

k = b  # b를 시작으로 연산의 횟수 확인
cnt = 0
while k >= a:
    if k == a:
        print(cnt + 1)
        break
    if k % 2 == 0:  
        k = k // 2 
        cnt += 1  # 연산 횟수 1 증가
    elif k % 10 == 1:
        k -= 1  
        k = k // 10
        cnt += 1  # 연산 횟수 1 증가

    else: 
        print(-1)
        break


if k < a:
    print(-1)


