board = [list(map(int, input().split())) for _ in range(10)]

# 최대 경우로 초기화
ans = 25

# 각 색종이마다 사용한 수
paper = [0] * 6


def is_possible(y, x, p):
    # 덮고자 하는 사이즈의 색종이가 남아있는지 확인
    if paper[p] == 5:
        return False

    # 범위 체크 ( 종이를 넘어선 안됨)
    if y + p > 10 or x + p > 10:
        return False
    # 색종이 크기만큼 덮어보고 0있으면 안됨
    for i in range(p):
        for j in range(p):
            if board[y + i][x + j] == 0:
                return False

    return True


def mark(y, x, p, cover):
    for i in range(p):
        for j in range(p):
            board[y + i][x + j] = cover  # 0으로 커버함

    if cover:
        paper[p] -= 1
    else:  # 0일 때 덮은 것임
        paper[p] += 1


def backtracking(y, x):
    global ans
    if y == 10:  # 맨 아래 행 도착
        ans = min(ans, sum(paper))
        return

    if x == 10:  # 끝 열에 도착하면 다음 행 탐색
        backtracking(y + 1, 0)
        return

    if board[y][x] == 0:  # 0이면 다음 칸으로
        backtracking(y, x + 1)
        return

    # 1을 만나면 각 종이를 몇개 써야하는지 계산
    for p in range(1, 6):
        if is_possible(y, x, p):  # cover 가능?
            # 색종이 cover 를 0으로 체크
            # 다른 색종이가 덮을 때 포함하지 않기 위해
            mark(y, x, p, 0)
            backtracking(y, x + 1)
            mark(y, x, p, 1)  # 다음 색종이를 위해 복구


backtracking(0, 0)

print(-1 if ans == 25 else ans)
