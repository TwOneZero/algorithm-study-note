import sys
from collections import Counter

input = sys.stdin.readline


# dict 대신 Counter 쓰면 dict 형태로 바로 계산해줌
# c = Counter(input())

# dict 로 알파벳 개수세기
in_str = list(input().rstrip())
d_alpha = dict()


for c in in_str:
    if c in d_alpha:
        d_alpha[c] += 1
    else:  # 초기화
        d_alpha[c] = 1

# 홀수 개인 알파벳이 두 개 이상이면 탈락
if sum(i % 2 for i in d_alpha.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''  #절반짜리
    mid = ''
    for k, v in sorted(d_alpha.items()):
        if v % 2:
            mid = k
        half += k * (v // 2) # 절반만 저장

    ans = half + mid
    ans += ''.join(reversed(half))
    print(ans)

