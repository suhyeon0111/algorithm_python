# 회문은 회문아니야!

import sys

palindrome = sys.stdin.readline().rstrip()

check_word = palindrome[::-1]  # 문자열 뒤집기
result = len(palindrome)  # 문자 길이

if palindrome == check_word:  # 회문이라면
    if palindrome.count(palindrome[0]) == result:  # 모두 같은 문자
        print(-1)
    else:
        print(result - 1)
else:  # 회문 아님
    print(len(palindrome))
