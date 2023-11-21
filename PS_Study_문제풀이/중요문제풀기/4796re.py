import sys

input = sys.stdin.readline

a = b = 0
cnt = 1

while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    a = V // P
    b = V % P
    print(f'Case {cnt}: {L * a + min(L, b)}')
    cnt += 1
