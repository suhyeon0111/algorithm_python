# 베스트셀러

from sys import stdin

n = int(stdin.readline())  # 하루동안 팔린 책의 개수

book = {}
for _ in range(n):
    name = stdin.readline()
    if name not in book:  # 처음 보는 책
        book[name] = 1
    else:
        book[name] += 1

result = []
target = max(book.values())  # 가장 많이 팔린 책
for i in book.keys():
    if book[i] == target:
        result.append(i)

result.sort()  # 가장 많이 팔린 책이 여러 개일 경우 사전 순으로 정렬
print(result[0])
