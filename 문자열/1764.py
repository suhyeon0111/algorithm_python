# 듣보잡

n, m = map(int, input().split())

name1 = set()
for _ in range(n):
    name1.add(input())

name2 = set()
for _ in range(m):
    name2.add(input())

result = sorted(list(name1 & name2))

print(len(result))

for i in result:
    print(i)


# 집합 자료형
# 교집합
# s1 & s2
# s1.intersection(s2)
