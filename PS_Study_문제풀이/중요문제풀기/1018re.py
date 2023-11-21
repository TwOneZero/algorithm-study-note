# 완전 탐색으로 풀기
# 최대로 칠해야 하는 수 : 8 * 8 = 64
# 기준점이 검정색 or 하얀색

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# N -> 세로 길이
# M -> 가로 길이
board = [input().rstrip() for _ in range(N)]

# print(board)

ans = 64  # 최대 일 때 -> 32 정도보다 크게 설정


# 색칠 하는 로직 함수 /  bw -> 8*8 자르는 기준 점( 맨왼쪽 맨위 )
def change_color(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:  # 인덱스가 홀수 -> 시작점이 W -> 짝수 인덱스가 W / 홀수 인덱스가 B
                # 다음 인덱스가 bw , 즉 같으면 색칠 -> cnt 증가
                if board[y + i][x + j] == bw:
                    cnt += 1
            else:  # 인덱스가 짝수 , 즉 !bw -> 그 다음이 !bw 이면 -> cnt 증가
                if board[y + i][x + j] != bw:
                    cnt += 1
    # 8 * 8 을 돌고 나서 ans 와 cnt 비교 후 작은 거 저장
    ans = min(ans, cnt)


# 8 * 8 보다 큰 만큼만 돌면 됨
# ex -> 10 * 8 : 3가지 경우의 수  -> N-7
for i in range(N - 7):
    for j in range(M - 7):
        # 기준점이 B일 때 or W일 때
        change_color(i, j, 'B')
        change_color(i, j, 'W')

print(ans)