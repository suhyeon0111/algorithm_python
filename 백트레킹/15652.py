# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4


import sys
n, m = map(int, sys.stdin.readline().split())   
number = []


 # 깊이
def backtracking(depth, index, n, m):
    if depth == m:        
        # 종료
        result = " ".join(map(str, number))
        print(result)
       
    else:
        for i in range(index, n + 1):

            number.append(i)
            backtracking(depth + 1, i, n, m)
            number.pop() #초기화

backtracking(0, 1, n, m)





