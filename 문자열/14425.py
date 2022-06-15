# 문자열 집합

n, m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input())

cnt = 0
for _ in range(m):
    word = input()
    if word in s:
        cnt += 1
print(cnt)


# result = s & s2
# print(len(result))
