import sys
from collections import deque

input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]


# print(board)
def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))  # 튜플 세번 째 인덱스는 몇 칸을 지났는 지 count
    while dq:
        y, x, d = dq.popleft()
        nd = d + 1
        # 도착했는지 체크
        if y == N -1 and x == M-1:
            return d
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


print(bfs())
