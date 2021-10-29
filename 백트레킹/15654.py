
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열



import sys

n, m = map(int, sys.stdin.readline().split())   
number = list(map(int, sys.stdin.readline().split()))
result = []             # 결과 값

# 정렬
number.sort()

def backtracking(depth, n, m):
    if depth == m:    
        print(" ".join(map(str, result)))

    else:
        for x in number:
            if x not in result:             # 자기 자신은 포함하면 안되기 때문
                result.append(x)    
                backtracking(depth + 1, n, m)
                result.pop()


backtracking(0, n, m)
