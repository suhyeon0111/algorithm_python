# 그룹 단어 체커

from sys import stdin

n = int(stdin.readline())

cnt = n  # 그룹 단어가 될 수 있는 단어의 최대 개수
for _ in range(n):
    word = stdin.readline()
    for i in range(len(word) - 1):
        # 문자가 달라질 때 비교
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]
            # i 인덱스 이후의 문자들을 복사하여 word[i]가 다시 나오는지 확인
            if word[i] in new_word:
                cnt -= 1
                break


print(cnt)  # 결과 출력
