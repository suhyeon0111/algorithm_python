# 팰린드롬 만들기
# 앞으로 읽나 뒤로 읽나 같은 문자열
# 첫째 줄에 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력

# 특정 인덱스에 리스트 요소 추가 => insert(idx, 요소)

s = input()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break

# s[i:][::-1]뒤집기

