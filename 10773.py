from sys import stdin

K = int(input())
stack = []

for i in range(K):
    num = int(input())  
    if num == 0:
        stack.pop()

    else:
        stack.append(num)

result = sum(stack)
print(result)

