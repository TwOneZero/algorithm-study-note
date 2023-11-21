# 1 ~ 6 개의 줄
# 줄마다 P 개의 프렛으로 나누어져 있음
# 프렛의 번호도 1 ~ P
# 한 번 누르거나 떼는 것을 손가락을 한 번 움직였다고 한다.
# 손가락의 가장 적게 움직이는 회수를 구하기
#
# 음의 수 N과 한 줄에 있는 프렛의 수 P가 주어진다.
# (1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)

import sys

input = sys.stdin.readline

# N 줄에 해당하는 배열 각 인덱스에 스택을 쌓아
# 스택 맨 위 숫자보다 큰 게 들어오면 그대로 쌓고
# 작은 게 들어오면 들어온 수가 제일 클 때까지 pop 후 스택에 저장

N, P = map(int, input().split())

# 최대 6개  1~6 인덱스
stk = [[] for _ in range(7)]
cnt = 0
# print(stk)

for _ in range(N):
    n, p = map(int, input().split())
    while stk[n] and stk[n][-1] > p:
        stk[n].pop()
        cnt += 1
    if not stk[n] or stk[n][-1] < p:
        stk[n].append(p)
        cnt += 1
    elif stk[n] and stk[n][-1] == p:
        continue


print(cnt)
