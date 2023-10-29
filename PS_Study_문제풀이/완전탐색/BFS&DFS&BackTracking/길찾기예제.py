from collections import deque

# 동 북 서 남
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 중복방문체크
chk = [[False] * 100 for _ in range(100)]
# 노드 최대 범위
N = int(input())


# 인덱스 허용 범위 체크 Boolean
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


# BFS
def bfs(start_y, start_x):
    q = deque()
    # 좌표 튜플로 저장
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        # 다음 좌표 설정
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            # 허용범위 and 처음 방문
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))


bfs(1, 1)
